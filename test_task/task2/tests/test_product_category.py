# file: tests/test_product_category.py
import pytest
from pyspark.sql import SparkSession
from pyspark.sql import Row

from task2.product_category import product_category_pairs

@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("product-category-tests")
        .getOrCreate()
    )
    yield spark
    spark.stop()

def to_set(df, cols=("product_name", "category_name")):
    return set([tuple(r[c] for c in cols) for r in df.collect()])

def test_pairs_with_and_without_categories(spark):
    products = spark.createDataFrame([
        Row(product_id=1, product_name="Milk"),
        Row(product_id=2, product_name="Bread"),
        Row(product_id=3, product_name="Coffee"),
        Row(product_id=4, product_name="Water"),
    ])

    categories = spark.createDataFrame([
        Row(category_id=10, category_name="Dairy"),
        Row(category_id=20, category_name="Bakery"),
        Row(category_id=30, category_name="Beverage"),
    ])

    product_categories = spark.createDataFrame([
        Row(product_id=1, category_id=10),  # Milk -> Dairy
        Row(product_id=3, category_id=30),  # Coffee -> Beverage
        Row(product_id=3, category_id=10),  # Coffee -> Dairy 

    ])

    result = product_category_pairs(products, categories, product_categories)

    expected = {
        ("Milk", "Dairy"),
        ("Coffee", "Beverage"),
        ("Coffee", "Dairy"),
        ("Bread", None),   # нет категорий
        ("Water", None),   # нет категорий
    }
    assert to_set(result) == expected

def test_deduplication_of_links(spark):
    products = spark.createDataFrame([
        Row(product_id=1, product_name="Milk"),
    ])
    categories = spark.createDataFrame([
        Row(category_id=10, category_name="Dairy"),
    ])

    product_categories = spark.createDataFrame([
        Row(product_id=1, category_id=10),
        Row(product_id=1, category_id=10),
    ])

    result = product_category_pairs(products, categories, product_categories)
    assert to_set(result) == {("Milk", "Dairy")}

def test_all_products_without_categories_when_links_empty(spark):
    products = spark.createDataFrame([
        Row(product_id=1, product_name="A"),
        Row(product_id=2, product_name="B"),
    ])
    categories = spark.createDataFrame([], schema="category_id INT, category_name STRING")
    product_categories = spark.createDataFrame([], schema="product_id INT, category_id INT")

    result = product_category_pairs(products, categories, product_categories)
    assert to_set(result) == {("A", None), ("B", None)}

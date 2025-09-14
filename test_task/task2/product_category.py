# product_category.py
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def product_category_pairs(
    products_df: DataFrame,          # product_id, product_name
    categories_df: DataFrame,        # category_id, category_name
    product_categories_df: DataFrame # product_id, category_id
) -> DataFrame:
    """
   один DataFrame со всеми парами (product_name, category_name),
    и также строки (product_name, NULL) для товаров без категорий

     колонки:
      - products_df:  product_id, product_name
      - categories_df: category_id, category_name
      - product_categories_df: product_id, category_id
    """
    p = products_df.select("product_id", "product_name").dropDuplicates()
    c = categories_df.select("category_id", "category_name").dropDuplicates()
    pc = product_categories_df.select("product_id", "category_id").dropDuplicates()

    joined = (
        p.alias("p")
         .join(pc.alias("pc"), F.col("p.product_id") == F.col("pc.product_id"), how="left")
         .join(c.alias("c"), F.col("pc.category_id") == F.col("c.category_id"), how="left")
         .select(F.col("p.product_name").alias("product_name"),
                 F.col("c.category_name").alias("category_name"))
    )

    return joined.dropDuplicates()

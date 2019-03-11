# Example ETL with no parameters - see etl() function

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, current_timestamp
from pipelines.utils import transformations, configmanagement as cm

spark = SparkSession.builder.getOrCreate()


def extract_Amazon(filePath):
    return spark.read.format("parquet").load(filePath)

def transform_Amazon(df):
    df = df.withColumn("time_stamp", lit(current_timestamp()))
    df = transformations.addDummyColumn(df)
    return df

def load_Amazon(df):
  spark.sql("DROP TABLE IF EXISTS amazon")
  df.write.format("delta").mode("overwrite").saveAsTable("amazon")
  return

def etl():
  #cm.setDatabase()
  df = extract_Amazon("/databricks-datasets/amazon/test4K")
  df = transform_Amazon(df)
  load_Amazon(df)
# Example ETL with a parameter - see etl() function
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, current_timestamp
from pipelines.utils import transformations, configmanagement as cm

spark = SparkSession.builder.getOrCreate()

def extract_Planes(filePath, year):
    print(cm.getSecret("DataThirst1","Secret1"))
    return spark.read.format("csv").option("header", "true").load(filePath).filter(col("year") == year)

def transform_Planes(df, dummyValue):
    df = df.withColumn("NewCol", lit(dummyValue)).filter(col("model").isNotNull())
    df = df.withColumn("time_stamp", lit(current_timestamp()))
    df = transformations.addDummyColumn(df)
    return df

def load_Planes(df):
  #cm.setDatabase()
  df.write.format("delta").mode("overwrite").saveAsTable("planes")
  return

def etl(year:int, dummyValue:int=99):
  df = extract_Planes("/databricks-datasets/asa/planes", year)
  df = transform_Planes(df, dummyValue)
  load_Planes(df)

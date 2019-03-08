# Example ETL with a parameter - see etl() function

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col
import os
import sys

spark = SparkSession.builder.getOrCreate()

# Tell python to look in the helpers folder for any modules that I try to import (ie the transformations module)
try:
  dirname = os.path.dirname(__file__)
  sys.path.insert(0, (os.path.join(dirname, '../helpers')))
except:
  print('ignoring')

import transformations

class planes(object):
  def __init__(self, x):
    self.x = x

  def extract_Planes(filePath, year):
      print(dbutils.secrets.get("DataThirst1","Test1"))
      return spark.read.format("csv").option("header", "true").load(filePath).filter(col("year") == year)

  def transform_Planes(df, dummyValue):
      df = df.withColumn("NewCol", lit(dummyValue)).filter(col("model").isNotNull())
      df = transformations.addDummyColumn(df)
      return df

  def load_Planes(df):
    df.write.format("delta").mode("append").saveAsTable("planes")
    return

  def etl(year:int, dummyValue:int=99):
    df = extract_Planes("/databricks-datasets/asa/planes", year)
    df = transform_Planes(df, dummyValue)
    load_Planes(df)

  # This function is not called in our application, it is here for debugging purposes only
  # If I execute this script then the process function will be called
  if __name__ == '__main__':
      from pyspark.dbutils import DBUtils
      dbutils = DBUtils(spark.sparkContext)
      etl(1980, 100)
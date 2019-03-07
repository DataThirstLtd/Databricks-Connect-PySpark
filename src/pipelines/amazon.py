# Example ETL with no parameters - see etl() function

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

class amazon(object):
  def __init__(self, x):
    self.x = x

def extract_Amazon(filePath):
    return spark.read.format("parquet").load(filePath)

def transform_Amazon(df):
    df = df.withColumn("NewCol", lit(0))
    df = transformations.addDummyColumn(df)
    return df

def load_Amazon(df):
  spark.sql("DROP TABLE IF EXISTS amazon")
  df.write.format("delta").mode("overwrite").saveAsTable("amazon")
  return

def etl():
  df = extract_Amazon("/databricks-datasets/amazon/test4K")
  df = transform_Amazon(df)
  load_Amazon(df)


# This function is not called in our application, it is here for debugging purposes only
# If I execute this script then the process function will be called
if __name__ == '__main__':
    etl()
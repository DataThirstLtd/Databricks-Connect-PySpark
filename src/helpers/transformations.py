
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
spark = SparkSession.builder.getOrCreate()

class transformations(object):
  def __init__(self, x):
    self.x = x


def addDummyColumn(df):
    df = df.withColumn("AnotherColumn", lit(0))
    return df
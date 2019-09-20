# This module is used for generic transformations that are reused across
# many pipelines. Examples would include:
#     Adding a Surrogate Key
#     SCD Type 1,2,4 etc helpers
#     Applying Keys to facts
#     Adding common metadata columns


from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.getOrCreate()

def addDummyColumn(df):
    df = df.withColumn("AnotherColumn", lit(0))
    return df

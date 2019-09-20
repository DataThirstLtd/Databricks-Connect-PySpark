from pipelines.jobs import planes, amazon
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
# Use this script to test executing the pipleines locally
# planes.etl(1980, 10)
amazon.etl()

df = spark.sql("SELECT * FROM amazon")
df.show()
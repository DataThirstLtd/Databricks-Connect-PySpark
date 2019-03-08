from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

class utils:
    def isLocal():
        setting = spark.conf.get("spark.master")
        if "local" in setting:
            return True
        else:
            return False
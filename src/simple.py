from pyspark.sql import SparkSession
#

spark = SparkSession.builder.getOrCreate()
#

def isLocal():
    setting = spark.conf.get("spark.master")
    if "local" in setting:
        return True
    else:
        return False


if isLocal():
    from pyspark.dbutils import DBUtils
    dbutils = DBUtils(spark.sparkContext)
    MySecret = "Set Locally"
else:
    MySecret = dbutils.secrets.get("DataThirst1","Test1")

print(MySecret)

#print(dbutils.secrets.get("DataThirst1","Test1"))

#print(spark.sparkContext.getConf().getAll())
#print(dbutils.notebook.getContext.apiToken.get.split("").mkString("<span/>")))

#print(dbutils.secrets.get("DataThirst1","Test1"))
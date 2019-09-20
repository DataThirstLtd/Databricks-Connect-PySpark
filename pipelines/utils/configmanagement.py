
import os
import json
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

def isLocal():
    spark = SparkSession.builder.getOrCreate()
    setting = spark.conf.get("spark.master")
    if "local" in setting:
        return True
    else:
        return False

def loadConfigFile():
    if isLocal():
        dirname = os.path.dirname(__file__)
        configFile = os.path.join(dirname, '../../configs/config.json')
    else:
        # Note this path must match the path in Deploy.ps1 parameter TargetDBFSFolderCode
        configFile = "/dbfs/DatabricksConnectDemo/Code/config.json"
    with open(configFile, 'r') as f:
        config = json.load(f)
    return config

def getConfigSetting(settingName):
    config = loadConfigFile()
    return config['Settings'][settingName]

def setDatabase():
    databaseName = getConfigSetting("DatabaseName")
    spark.sql("CREATE DATABASE IF NOT EXISTS " + databaseName)
    spark.sql("USE " + databaseName)
    return
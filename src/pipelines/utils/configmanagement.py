
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
        configFile = "/MyApp/config.json"
    with open(configFile, 'r') as f:
        config = json.load(f)
    return config

def getMockSecret(scope,secret):
    config = loadConfigFile()['MockSecrets']
    scopeConfig = [x['Secrets'] for x in config if x['Scope'] == scope]
    return scopeConfig[0][secret]

def getDatabricksSecret(scope,secret):
    return dbutils.secrets.get("DataThirst1","Test1")

def getSecret(scope,secret):
    if isLocal():
        res = getMockSecret(scope,secret)
    else:
        res = getDatabricksSecret(scope,secret)
    return res

def getConfigSetting(settingName):
    config = loadConfigFile()
    return config['Settings'][settingName]

def setDatabase():
    databaseName = getConfigSetting("DatabaseName")
    spark.sql("CREATE DATABASE IF NOT EXISTS " + databaseName)
    spark.sql("USE " + databaseName)
    return
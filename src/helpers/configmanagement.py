import os
import json

class configmanagement(object):
    def __init__(self, x):
        self.x = x

    def loadConfigFile():
        if isLocal():
            dirname = os.path.dirname(__file__)
            configFile = os.path.join(dirname, '../configs/config.json')
        else:
            configFile = "/MyApp/config.json"
        with open(configFile, 'r') as f:
            config = json.load(f)
        return config

    def getMockSecret(scope,secret):
        config = loadConfigFile()
        scopeConfig = [x['Secrets'] for x in config if x['Scope'] == scope]
        return scopeConfig[0][secret]

    def getDatabricksSecret(scope,secret):
        return dbutils.secrets.get("DataThirst1","Test1")

    def getSecret(scope,secret):
        if isLocal():
            res = getDatabricksSecret(scope,secret)
        else:
            res = getMockSecret(scope,secret)
        return res

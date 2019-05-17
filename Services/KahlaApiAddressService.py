from pickle import dump
from pickle import load
from Services.HomeFloderConfig import HomeFloderConfig
from package import stable

class KahlaApiAddressService(object):
    serverAddress = None

    # True: 使用master版本
    # False: 使用stagging版本
    
    def __init__(self):
        if stable == True:
            self.serverAddress = "https://server.kahla.app"
        else:
            self.serverAddress = "https://staging.server.kahla.app"

    def getaddress(self):
        return self.serverAddress
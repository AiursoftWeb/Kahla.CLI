from pickle import dump
from pickle import load
from Services.HomeFloderConfig import HomeFloderConfig

class KahlaApiAddressService(object):
    serverAddress = None

    # True: 使用master版本
    # False: 使用stagging版本
    
    def __init__(self):
        try:
            with open("{0}/user.apiaddress.bin".format(HomeFloderConfig().getconfigpath()), "rb") as f:
                data = load(f)
                if data == True:
                    self.serverAddress = "https://server.kahla.app"
                else:
                    self.serverAddress = "https://staging.server.kahla.app"
        except:
            self.serverAddress = "https://server.kahla.app"
        if self.serverAddress == None:
            self.serverAddress = "https://server.kahla.app"

    def usemaster(self):
        with open("{0}/user.apiaddress.bin".format(HomeFloderConfig().getconfigpath()), "wb") as f:
            dump(True, f)

    def usestagging(self):
        with open("{0}/user.apiaddress.bin".format(HomeFloderConfig().getconfigpath()), "wb") as f:
            dump(False, f)

    def getaddress(self):
        return self.serverAddress
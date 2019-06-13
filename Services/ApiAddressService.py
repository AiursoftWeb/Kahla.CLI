from package import stable


class ApiAddressService(object):
    def __init__(self):
        if stable:
            self.serverAddress = "https://server.kahla.app"
        else:
            self.serverAddress = "https://staging.server.kahla.app"

    def getaddress(self):
        return self.serverAddress

import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaGroupApiService(object):
    def __init__(self):
        self.apiaddress = KahlaApiAddressService()
        self.storagecookie = StorageCookieService()
    
    def LeaveGroup(self, groupname):
        r = requests.post("{0}/Groups/LeaveGroup".format(self.apiaddress.getaddress()), data={
            "groupName": groupname
        },
        cookies=self.storagecookie.get())

        return r
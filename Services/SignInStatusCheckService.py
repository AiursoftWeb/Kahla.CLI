from Services.StorageCookieService import StorageCookieService
from Services.ApiAddressService import ApiAddressService
from Services.HomeFloderConfig import HomeFloderConfig
import os
import requests
import json


class SignInStatusCheckService(object):
    def __init__(self):
        self.storagecookie = StorageCookieService()
        self.apiaddress = ApiAddressService()

    def check(self):
        if os.path.exists(
                "{0}/user.cookie.bin".format(HomeFloderConfig().getconfigpath())):
            cookies = self.storagecookie.get()
            result = json.loads(requests.post("{0}/Auth/SignInStatus".format(self.apiaddress.getaddress()),
                                              cookies=cookies).text)
            if result["value"]:
                return True
            else:
                return False
        else:
            return False

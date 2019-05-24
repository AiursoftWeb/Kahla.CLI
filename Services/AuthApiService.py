import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class AuthApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def Version(self):
        r = requests.get(
            "{0}/Auth/Version".format(self.apiaddress.getaddress()))

        return r

    def AuthByPassword(self, email, password):
        r = requests.post("{0}/Auth/AuthByPassword".format(self.apiaddress.getaddress()), data={
            "Email": email,
            "Password": password
        })

        return r

    def InitPusher(self):
        r = requests.get("{0}/Auth/InitPusher".format(self.apiaddress.getaddress()),
                         cookies=self.storagecookie.get())

        return r

    def Me(self):
        r = requests.get(
            "{0}/Auth/Me".format(self.apiaddress.getaddress()), cookies=self.storagecookie.get())

        return r

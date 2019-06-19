import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class AuthApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def Version(self):
        return requests.get("{0}/Auth/Version".format(self.apiaddress.getaddress()))

    def AuthByPassword(self, email, password):
        return requests.post("{0}/Auth/AuthByPassword".format(self.apiaddress.getaddress()), data={
            "Email": email,
            "Password": password
        })

    def InitPusher(self):
        return requests.get("{0}/Auth/InitPusher".format(self.apiaddress.getaddress()),
                         cookies=self.storagecookie.get())

    def SignInStatus(self):
        return requests.get("{0}/Auth/SignInStatus".format(self.apiaddress.getaddress(),
                         cookies=self.storagecookie.get()))

    def Me(self):
        return requests.get(
            "{0}/Auth/Me".format(self.apiaddress.getaddress()), 
                cookies=self.storagecookie.get())
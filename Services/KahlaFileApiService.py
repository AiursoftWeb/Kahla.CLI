import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService


class KahlaFileApiService(object):
    def __init__(self):
        self.apiaddress = KahlaApiAddressService()
        self.storagecookie = StorageCookieService()

    def FileDownloadAddress(self, filekey):
        r = requests.post("{0}/Files/FileDownloadAddress".format(self.apiaddress.getaddress()),
                          data={
            "FileKey": filekey
        },
            cookies=self.storagecookie.get())

        return r

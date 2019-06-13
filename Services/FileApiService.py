import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class FileApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def FileDownloadAddress(self, filekey):
        return requests.post("{0}/Files/FileDownloadAddress".format(self.apiaddress.getaddress()), data={
                "FileKey": filekey
            }, cookies=self.storagecookie.get())

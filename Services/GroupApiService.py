import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class GroupApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def LeaveGroup(self, groupname):
        return requests.post("{0}/Groups/LeaveGroup".format(self.apiaddress.getaddress()), data={
                "groupName": groupname
            }, cookies=self.storagecookie.get())

import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class FriendShipApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def Mine(self):
        return requests.get("{0}/Friendship/Mine".format(self.apiaddress.getaddress()),
                         cookies=self.storagecookie.get())

    def UserDetail(self, userid):
        return requests.get("{0}/Friendship/UserDetail?id={1}".format(self.apiaddress.getaddress(), str(userid)),
                         cookies=self.storagecookie.get())

    def DeleteFriend(self, userid):
        return requests.post("{0}/Friendship/DeleteFriend".format(self.apiaddress.getaddress()), data={
                "id": str(userid)
            }, cookies=self.storagecookie.get())

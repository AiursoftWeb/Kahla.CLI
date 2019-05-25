import requests
from Services.ApiAddressService import ApiAddressService
from Services.StorageCookieService import StorageCookieService


class FriendShipApiService(object):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.storagecookie = StorageCookieService()

    def Friends(self, take=100000):
        r = requests.get("{0}/Friendship/MyFriends?orderByName=true&Take={1}".format(self.apiaddress.getaddress(), take),
                         cookies=self.storagecookie.get())

        return r

    def UserDetail(self, userid):
        r = requests.get("{0}/Friendship/UserDetail?id={1}".format(self.apiaddress.getaddress(), str(userid)),
                         cookies=self.storagecookie.get())

        return r

    def DeleteFriend(self, userid):
        r = requests.post("{0}/Friendship/DeleteFriend".format(self.apiaddress.getaddress()), data={
            "id": str(userid)
        },
            cookies=self.storagecookie.get())

        return r
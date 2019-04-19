import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaFriendShipApiService(object):
    def __init__(self):
        self.apiaddress = KahlaApiAddressService()
        self.storagecookie = StorageCookieService()
    
    def Friends(self):
        r = requests.get("{0}/Friendship/MyFriends?orderByName=true".format(self.apiaddress.getaddress()),
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
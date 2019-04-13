import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaFriendShipApiService(object):
	apiaddress = None

	def __init__(self):
		self.apiaddress = KahlaApiAddressService()
		self.storagecookie = StorageCookieService()
	
	def Friends(self):
		r = requests.get("{0}/Friendship/MyFriends?orderByName=true".format(self.apiaddress.getaddress()),
				   cookies=self.storagecookie.get())
		
		return r
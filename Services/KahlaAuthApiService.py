import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaAuthApiService(object):
	apiaddress = None

	def __init__(self):
		self.apiaddress = KahlaApiAddressService()
		self.storagecookie = StorageCookieService()
	
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
from Services.StorageCookieService import StorageCookieService
from Services.KahlaApiAddressService import KahlaApiAddressService
import os
import requests
import json

class KahlaSignInStatusCheckService(object):
	def __init__(self):
		self.storagecookie = StorageCookieService()
		self.apiaddress = KahlaApiAddressService()

	def check(self):
		if os.path.exists("./user.cookie.bin") == True:
			cookies = self.storagecookie.get()
			result = json.loads(requests.post("{0}/Auth/SignInStatus".format(self.apiaddress.getaddress()), 
									 cookies=cookies).text)
			if result["value"] == True:
				return True
			else:
				return False
		else:
			return False
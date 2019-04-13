import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService

class KahlaAuthApiService(object):
	apiaddress = None

	def __init__(self):
		self.apiaddress = KahlaApiAddressService()
	
	def AuthByPassword(self, email, password):
		r = requests.post("{0}/Auth/AuthByPassword".format(self.apiaddress.getaddress()), data={
			"Email": email,
			"Password": password
		})
		
		return r
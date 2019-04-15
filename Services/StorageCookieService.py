import pickle
from Services.HomeFloderConfig import HomeFloderConfig

class StorageCookieService(object):
	def __init__(self):
		self.path = "{0}/user.cookie.bin".format(HomeFloderConfig().getconfigpath())

	def storage(self, cookie):
		with open(self.path, "wb") as f:
			pickle.dump(cookie, f)

	def get(self):
		with open(self.path, "rb") as f:
			return pickle.load(f)
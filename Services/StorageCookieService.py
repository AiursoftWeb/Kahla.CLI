import pickle

class StorageCookieService(object):
	def __init__(self):
		self.path = "./user.cookie.bin"

	def storage(self, cookie):
		with open(self.path, "wb") as f:
			pickle.dump(cookie, f)

	def get(self):
		with open(self.path, "rb") as f:
			return pickle.load(f)
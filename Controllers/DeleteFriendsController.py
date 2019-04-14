from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Library.cryptojs import *
import json

class DeleteFriendsController(Controller):
	def __init__(self):
		self.friendshipservice = KahlaFriendShipApiService()
		self.checkstatusservice = KahlaSignInStatusCheckService()

	# 定义参数
	def get_options(self):
		return [
			Option('-u', '--username', dest='username'),	
		]

	# 处理输入参数, 检查合法性
	def run(self, username):
		# 这条必须编写, 并且带上传入的参数
		self.compute(username)

	# 处理业务逻辑
	def main(self, username):
		if self.checkstatusservice.check() == True:
			friends = self.friendshipservice.Friends()
			friendsdata = json.loads(friends.text)["items"]
			for x in friendsdata:
				if x["displayName"] == username:
					r = self.friendshipservice.DeleteFriend(x["userId"])
					r = json.loads(r.text)
					if r["code"] == 0:
    						return ""
					else:
    						return r["message"]

			return "The user name you entered is incorrect!"
		else:
			return "You are not logged in!"
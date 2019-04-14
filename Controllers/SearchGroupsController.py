from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Library.cryptojs import *
import json

class SearchGroupsController(Controller):
	def __init__(self):
		self.friendshipservice = KahlaFriendShipApiService()
		self.checkstatusservice = KahlaSignInStatusCheckService()

	# 定义参数
	def get_options(self):
		return [
			Option('-si', '--searchinput', dest='searchinput'),	
		]

	# 处理输入参数, 检查合法性
	def run(self, searchinput):
		# 这条必须编写, 并且带上传入的参数
		self.compute(searchinput)

	# 处理业务逻辑
	def main(self, searchinput):
		if self.checkstatusservice.check() == True:
			friends = self.friendshipservice.Friends()
			friendsdata = json.loads(friends.text)["items"]
			datas = []
			for x in friendsdata:
					if x["displayName"].lower().find(searchinput.lower()) >= 0:
							if x["discriminator"] != "PrivateConversation":
								pingdata = "{0}".format(x["displayName"])
								datas.append(pingdata)
			return datas
		else:
			return ["You are not logged in!"]
from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
import json

class LoginController(Controller):
	authapiservice = None
	storagecookie = None

	def __init__(self):
		self.authapiservice = KahlaAuthApiService()
		self.storagecookie = StorageCookieService()

	# 定义参数
	def get_options(self):
		return [
            Option('-e', '--email', dest='email'),
			Option('-p', '--password', dest='password')
        ]

	# 处理输入参数, 检查合法性
	def run(self, email, password):
		# 这条必须编写, 并且带上传入的参数
		self.compute(email, password)

	# 处理业务逻辑
	def main(self, email, password):
		siginresult = self.authapiservice.AuthByPassword(email, password)
		siginresultdict = dict(json.loads(siginresult.text))
		if siginresultdict["code"] == 0:
			self.storagecookie.storage(siginresult.cookies)
			return ""
		else:
			return siginresultdict["message"]
from flask_script import Option
from Services.KahlaApiAddressService import KahlaApiAddressService
from Library.Controller import Controller

class UseStaggingController(Controller):
	apiaddress = None

	def __init__(self):
		self.apiaddress = KahlaApiAddressService()

	# 定义参数
	def get_options(self):
		return []

	# 处理输入参数, 检查合法性
	def run(self):
		# 这条必须编写, 并且带上传入的参数
		self.compute()

	# 处理业务逻辑
	def main(self):
		self.apiaddress.usestagging()
		return {}

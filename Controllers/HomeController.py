from flask_script import Option
from Library.Controller import Controller

class HomeController(Controller):
	def get_options(self):
		return [
            Option('-p', '--pg', dest='pg', default="dfssadff"),
        ]

	# 处理输入参数, 检查合法性
	def run(self, pg):
		# 这条必须编写, 并且带上传入的参数
		self.compute(pg)

	# 处理业务逻辑
	def main(self, pg):
		return pg
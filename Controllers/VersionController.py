from flask_script import Option
from Library.Controller import Controller
import json
import requests

class VersionController(Controller):
    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    def main(self):
        r = requests.get("https://raw.githubusercontent.com/AiursoftWeb/Kahla.CLI/dev/package.json")
        data = json.loads(r.text)
        return data

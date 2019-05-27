from Library.Controller import Controller
import json
from Services.AuthApiService import AuthApiService
from package import version


class VersionController(Controller):
    def __init__(self):
        self.authapiservice = AuthApiService()

    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    def main(self):
        data = {}
        data["version"] = version
        d = self.authapiservice.Version()
        data["latestVersion"] = json.loads(d.text)["LatestCLIVersion"]
        return data

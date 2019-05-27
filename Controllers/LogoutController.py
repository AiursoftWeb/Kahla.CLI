from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.HomeFloderConfig import HomeFloderConfig
import os


class LogoutController(Controller):
    def __init__(self):
        self.checksignstatus = SignInStatusCheckService()
        self.homeconfig = HomeFloderConfig()

    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    def main(self):
        if self.checksignstatus.check():
            try:
                os.remove(
                    "{0}/user.cookie.bin".format(self.homeconfig.getconfigpath()))
                return ""
            except BaseException:
                return "You are not logged in!"
        else:
            return "You are not logged in!"

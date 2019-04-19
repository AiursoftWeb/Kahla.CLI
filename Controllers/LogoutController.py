from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.HomeFloderConfig import HomeFloderConfig
import json
import os

class LogoutController(Controller):
    def __init__(self):
        self.checksignstatus = KahlaSignInStatusCheckService()
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
        if self.checksignstatus.check() == True:
            try:
                os.remove("{0}/user.cookie.bin".format(self.homeconfig.getconfigpath()))
                return ""
            except:
                return "You are not logged in!"
        else:
            return "You are not logged in!"
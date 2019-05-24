from Services.ApiAddressService import ApiAddressService
from Services.AuthApiService import AuthApiService
from Listener.KahlaWebSocketListener import KahlaWebsocketListener
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
import json


class ListenController(Controller):
    def __init__(self):
        self.apiaddress = ApiAddressService()
        self.authapiservice = AuthApiService()
        self.checkstatusservice = SignInStatusCheckService()

    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    def main(self):
        if self.checkstatusservice.check():
            r = json.loads(self.authapiservice.InitPusher().text)
            self.listenerkahla = KahlaWebsocketListener(r["serverPath"])
            self.listenerkahla.connect()
            try:
                self.listenerkahla.run_forever()
                return ""
            except KeyboardInterrupt:
                self.listenerkahla.close()
                return ""
        else:
            return "You are not logged in!"

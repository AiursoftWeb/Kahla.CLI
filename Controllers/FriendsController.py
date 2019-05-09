from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Library.cryptojs import *
import json

class FriendsController(Controller):
    def __init__(self):
        self.friendshipservice = KahlaFriendShipApiService()
        self.checkstatusservice = KahlaSignInStatusCheckService()

    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    def main(self):
        if self.checkstatusservice.check() == True:
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            datas = []
            for x in friendsdata:
                if x["discriminator"] != "GroupConversation":
                    datas.append(x["displayName"])
            return datas
        else:
            return ["You are not logged in!"]
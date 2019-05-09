from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Services.KahlaGroupApiService import KahlaGroupApiService
from Library.cryptojs import *
import json

class LeaveGroupsController(Controller):
    def __init__(self):
        self.friendshipservice = KahlaFriendShipApiService()
        self.groupservice = KahlaGroupApiService
        self.checkstatusservice = KahlaSignInStatusCheckService()

    # 定义参数
    def get_options(self):
        return [
            Option('-g', '--group', dest='group'),  
        ]

    # 处理输入参数, 检查合法性
    def run(self, group):
        # 这条必须编写, 并且带上传入的参数
        self.compute(group)

    # 处理业务逻辑
    def main(self, group):
        if self.checkstatusservice.check() == True:
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            for x in friendsdata:
                if x["displayName"] == group:
                    if x["discriminator"] == "GroupConversation":
                        self.groupservice.LeaveGroup(x["displayName"])
                        return ""

            return "The user name you entered is incorrect!"
        else:
            return "You are not logged in!"
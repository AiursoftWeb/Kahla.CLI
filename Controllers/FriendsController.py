from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
import json


class FriendsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
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
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            datas = []
            for x in friendsdata:
                if x["discriminator"] != "GroupConversation":
                   datas.append(x["displayName"])
            return datas
        else:
            return ["You are not logged in!"]

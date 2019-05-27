from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
from Services.GroupApiService import GroupApiService
import json


class LeaveGroupsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.groupservice = GroupApiService
        self.checkstatusservice = SignInStatusCheckService()

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
        if self.checkstatusservice.check():
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

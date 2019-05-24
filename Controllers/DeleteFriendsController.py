from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
from Checks.DeleteFriendsChecker import DeleteFriendsChecker
import json


class DeleteFriendsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.checkstatusservice = SignInStatusCheckService()

    # 定义参数
    def get_options(self):
        return [
            Option('-u', '--username', dest='username'),
        ]

    # 处理输入参数, 检查合法性
    def run(self, username):
        DeleteFriendsChecker.Check(username)
        # 这条必须编写, 并且带上传入的参数
        self.compute(username)

    # 处理业务逻辑
    def main(self, username):
        if self.checkstatusservice.check():
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            for x in friendsdata:
                if x["displayName"] == username:
                    r = self.DeleteFriend(x["userId"])
                    r = json.loads(r.text)
                    if r["code"] == 0:
                        return ""
                    else:
                        return r["message"]

            return "The user name you entered is incorrect!"
        else:
            return "You are not logged in!"

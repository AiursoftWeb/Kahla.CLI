from flask_script import Option
from Library.Controller import Controller
from Services.FriendShipApiService import FriendShipApiService
from Checks.DeleteFriendsChecker import DeleteFriendsChecker
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class DeleteFriendsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()

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
    @loginchecker
    def main(self, username):
        friendslist = self.friendshipservice.Friends()
        friendslist = json.loads(friendslist.text)["items"]
        for x in friendslist:
            if x["displayName"] == username:
                err = self.DeleteFriend(x["userId"])
                err = json.loads(err.text)
                if err["code"] == 0:
                    return ""
                else:
                    return err["message"]

        return "The user name you entered is incorrect!"
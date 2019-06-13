from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
from Checks.SearchFriendsChecker import SearchFriendsChecker
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class SearchFriendsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.checkstatusservice = SignInStatusCheckService()

    # 定义参数
    def get_options(self):
        return [
            Option('-si', '--searchinput', dest='searchinput'),
        ]

    # 处理输入参数, 检查合法性
    def run(self, searchinput):
        SearchFriendsChecker.Check(searchinput)
        # 这条必须编写, 并且带上传入的参数
        self.compute(searchinput)

    # 处理业务逻辑
    @loginchecker
    def main(self, searchinput):
        friends = self.friendshipservice.Friends()
        friendslist = json.loads(friends.text)["items"]
        datas = []
        for x in friendslist:
            if x["displayName"].lower().find(searchinput.lower()) >= 0:
                if x["discriminator"] != "GroupConversation":
                    datas.append("{0}".format(x["displayName"]))
        
        return datas

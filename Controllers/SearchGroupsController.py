from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
from Checks.SearchGroupsChecker import SearchGroupsChecker
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class SearchGroupsController(Controller):
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
        SearchGroupsChecker.Check(searchinput)
        # 这条必须编写, 并且带上传入的参数
        self.compute(searchinput)

    # 处理业务逻辑
    @loginchecker
    def main(self, searchinput):
        mines = self.friendshipservice.Mine()
        friendslist = json.loads(mines.text)["groups"]
        datas = []
        for x in friendslist:
            if x["name"].lower().find(searchinput.lower()) >= 0:
                datas.append(x["name"])

        return datas

from flask_script import Option
from Library.Controller import Controller
from Services.FriendShipApiService import FriendShipApiService
from Services.GroupApiService import GroupApiService
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class LeaveGroupsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.groupservice = GroupApiService()

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
    @loginchecker
    def main(self, group):
        mines = self.friendshipservice.Mine()
        friendslist = json.loads(mines.text)["groups"]
        for x in friendslist:
            if x["name"] == group:
                err = self.groupservice.LeaveGroup(x["name"])
                err = json.loads(err.text)

                if err["code"] == 0:
                    return ""
                else:
                    return err["message"]

        return "The user name you entered is incorrect!"
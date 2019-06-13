from Library.Controller import Controller
from Services.FriendShipApiService import FriendShipApiService
from Services.GroupApiService import GroupApiService
import json
from Decorators.LoginStatusCheckDecorator import loginchecker

class GroupsController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.groupserivce = GroupApiService()

    # 定义参数
    def get_options(self):
        return []

    # 处理输入参数, 检查合法性
    def run(self):
        # 这条必须编写, 并且带上传入的参数
        self.compute()

    # 处理业务逻辑
    @loginchecker
    def main(self):
        mines = self.friendshipservice.Mine()
        friendslist = json.loads(mines.text)["groups"]
        datas = []
        for x in friendslist:
            datas.append(x["name"])
        return datas

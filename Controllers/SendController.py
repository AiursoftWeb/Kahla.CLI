from flask_script import Option
from Library.Controller import Controller
from Services.SignInStatusCheckService import SignInStatusCheckService
from Services.FriendShipApiService import FriendShipApiService
from Services.ConversationApiService import ConversationApiService
from Checks.SendChecker import SendChecker
from Library.cryptojs import encrypt
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class SendController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.checkstatusservice = SignInStatusCheckService()
        self.conversionservice = ConversationApiService()

    # 定义参数
    def get_options(self):
        return [
            Option('-u', '--username', dest='username'),
            Option('-m', '--message', dest='message')
        ]

    # 处理输入参数, 检查合法性
    def run(self, username, message):
        SendChecker.Check(username, message)
        # 这条必须编写, 并且带上传入的参数
        self.compute(username, message)

    # 处理业务逻辑
    @loginchecker
    def main(self, username, message):
            friends = self.friendshipservice.Friends()
            friendslist = json.loads(friends.text)["items"]
            for user in friendslist:
                if user['displayName'] == username:
                    message = encrypt(
                        bytes(
                            message,
                            "utf-8"),
                        bytes(
                            user["aesKey"],
                            "utf-8"))
                    err = self.conversionservice.SendMessage(user['conversationId'], message)
                    err = json.loads(err.text)
                    if err["code"] == 0:
                        return ""
                    else:
                        return err["message"]

            return "Your user name is incorrect!"

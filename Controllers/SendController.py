from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Services.KahlaConversationApiService import KahlaConversationApiService
from Checks.SendChecker import SendChecker
from Library.cryptojs import *
import json


class SendController(Controller):
    def __init__(self):
        self.friendshipservice = KahlaFriendShipApiService()
        self.checkstatusservice = KahlaSignInStatusCheckService()
        self.conversionservice = KahlaConversationApiService()

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
    def main(self, username, message):
        if self.checkstatusservice.check() == True:
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            for x in friendsdata:
                if x['displayName'] == username:
                    message = encrypt(bytes(message, "utf-8"), bytes(x["aesKey"], "utf-8"))
                    r = self.conversionservice.SendMessage(x['conversationId'], message)
                    resultdata = json.loads(r.text)
                    if resultdata["code"] == 0:
                        return ""
                    else:
                        return "The message could not be sent successfully!"
            
            return "Your user name is incorrect!"
        else:
            return "You are not logged in!"

from flask_script import Option
from Library.Controller import Controller
from Services.AuthApiService import AuthApiService
from Services.FriendShipApiService import FriendShipApiService
from Services.ConversationApiService import ConversationApiService
from Library.processmessage import ProcessMessage
from Checks.GetMessagesChecker import GetMessagesChecker
from Library.cryptojs import decrypt
import json
from Decorators.LoginStatusCheckDecorator import loginchecker


class GetMessagesController(Controller):
    def __init__(self):
        self.friendshipservice = FriendShipApiService()
        self.conversionservice = ConversationApiService()
        self.authservice = AuthApiService()
        self.processmessage = ProcessMessage()

    # 定义参数
    def get_options(self):
        return [
            Option('-u', '--username', dest='username'),
            Option('-t', '--take', dest='take', default="15")
        ]

    # 处理输入参数, 检查合法性
    def run(self, username, take):
        GetMessagesChecker.Check(username, take)
        # 这条必须编写, 并且带上传入的参数
        self.compute(username, take)

    # 处理业务逻辑
    @loginchecker
    def main(self, username, take):
        friends = self.conversionservice.All()
        friendsdata = json.loads(friends.text)["items"]
        datas = []
        for x in friendsdata:
            if x['displayName'] == username:
                me = json.loads(self.authservice.Me().text)["value"]
                r = self.conversionservice.GetMesssages(x['conversationId'], take)
                resultdata = json.loads(r.text)
                if resultdata["code"] == 0:
                    for xx in resultdata["items"]:
                        if x["discriminator"] == "PrivateConversation":
                            if xx["senderId"] != me["id"]:
                                result = str(
                                    decrypt(
                                        bytes(
                                            xx["content"],
                                            "UTF-8"),
                                        bytes(
                                            x["aesKey"],
                                            "UTF-8")),
                                    "UTF-8")
                                result = self.processmessage.processMessage(result)
                                datas.append("{0} | {1}".format(x["displayName"], result))
                            else:
                                result = str(
                                    decrypt(
                                        bytes(
                                            xx["content"],
                                            "UTF-8"),
                                        bytes(
                                            x["aesKey"],
                                            "UTF-8")),
                                    "UTF-8")
                                result = self.processmessage.processMessage(result)
                                datas.append("{0} | {1}".format(me["nickName"], result))
                        else:
                            data = json.loads(
                                self.friendshipservice.UserDetail(
                                    xx['senderId']).text)["user"]
                            result = str(
                                decrypt(
                                    bytes(
                                        xx["content"],
                                        "UTF-8"),
                                    bytes(
                                        x["aesKey"],
                                        "UTF-8")),
                                "UTF-8")
                            result = self.processmessage.processMessage(result)
                            datas.append(
                                "{0} | {1} | {2}".format(
                                    x["displayName"], data["nickName"], result))
                    return datas
                else:
                    return ["unknown error!"]

        return ["Your user name is incorrect!"]

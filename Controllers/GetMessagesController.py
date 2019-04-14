from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Services.KahlaConversationApiService import KahlaConversationApiService
from Services.KahlaAuthApiService import KahlaAuthApiService
from Library.cryptojs import *
import json


class GetMessagesController(Controller):
    def __init__(self):
	    self.friendshipservice = KahlaFriendShipApiService()
	    self.checkstatusservice = KahlaSignInStatusCheckService()
	    self.conversionservice = KahlaConversationApiService()

    # 定义参数
    def get_options(self):
	    return [
			Option('-u', '--username', dest='username'),
			Option('-t', '--take', dest='take')
	    ]

	# 处理输入参数, 检查合法性
    def run(self, username, take):
        # 这条必须编写, 并且带上传入的参数
        self.compute(username, take)

    # 处理消息[检查消息类型]
    def processMessage(self, message):
        if message.find("[img]") >= 0:
            message = message.split("]")[1].split("-")[0]
            message = "Photo | https://oss.aiursoft.com/download/fromkey/{0}".format(message)
            return message
        
        if message.find("[video]") >= 0:
            message = message.split("]")[1]
            message = "Video | https://oss.aiursoft.com/download/fromkey/{0}".format(message)
            return message

        if message.find("[file]") >= 0:
            data = message.split("]")[1].split("-")
            fileuri = self.conversionservice.FileDownloadAddress(data[0])
            message = "File | {2} | {0} | {1}".format(data[1], data[2], json.loads(fileuri.text)["downloadPath"])
            return message

        return "Text | {0}".format(message)

	# 处理业务逻辑
    def main(self, username, take):
        if self.checkstatusservice.check() == True:
            friends = self.friendshipservice.Friends()
            friendsdata = json.loads(friends.text)["items"]
            datas = []
            for x in friendsdata:
                if x['displayName'] == username:
                    me = json.loads(self.friendshipservice.Me().text)["value"]
                    r = self.conversionservice.GetMesssages(x['conversationId'], take)
                    resultdata = json.loads(r.text)
                    if resultdata["code"] == 0:
                        for xx in resultdata["items"]:
                            if x["discriminator"] == "PrivateConversation":
                                if xx["senderId"] != me["id"]:
                                    result = str(decrypt(bytes(xx["content"], "UTF-8"), bytes(x["aesKey"], "UTF-8")), "UTF-8")
                                    result = self.processMessage(result)
                                    datas.append("{0} | {1}".format(x["displayName"], result))
                                else:
                                    result = str(decrypt(bytes(xx["content"], "UTF-8"), bytes(x["aesKey"], "UTF-8")), "UTF-8")
                                    result = self.processMessage(result)
                                    datas.append("{0} | {1}".format(me["nickName"], result))                    
                            else:
                                data = json.loads(self.friendshipservice.UserDetail(xx['senderId']).text)["user"]
                                result = str(decrypt(bytes(xx["content"], "UTF-8"), bytes(x["aesKey"], "UTF-8")), "UTF-8")
                                result = self.processMessage(result)
                                datas.append("{0} | {1} | {2}".format(x["displayName"], data["nickName"], result))
                        return datas
                    else:
                        return ["unknown error!"]
			
            return ["Your user name is incorrect!"]
        else:
            return ["You are not logged in!"]

from ws4py.client.threadedclient import WebSocketClient
from Library.cryptojs import *
from Library.timeconvert import *
from Services.KahlaFriendShipApiService import KahlaFriendShipApiService
from Services.KahlaConversationApiService import KahlaConversationApiService
from Library.processmessage import ProcessMessage
import json

class KahlaWebsocketListener(WebSocketClient):
    def received_message(self, message):
        self.processmessage = ProcessMessage()
        self.kfs = KahlaFriendShipApiService()
        me = self.kfs.Me()
        me = json.loads(me.text)["value"]
        messagedata = json.loads(str(message))
        if messagedata["typeDescription"] == "NewMessage":
            message = str(decrypt(bytes(messagedata["content"], "UTF-8"), bytes(messagedata["aesKey"], "UTF-8")), "UTF-8")
            message = self.processmessage.processMessage(message)
            print("{0} | {1}".format(messagedata["sender"]["nickName"], message))
            return
        
        if messagedata["typeDescription"] == "WereDeletedEvent":
            print("The {0} deleted you from his friends.".format(messagedata["trigger"]["nickName"]))
            return
        
        if messagedata["typeDescription"] == "NewFriendRequestEvent":
            print("The {0} wants to be your friend.".format(messagedata["requester"]["nickName"]))
            return
        
        if messagedata["typeDescription"] == "FriendAcceptedEvent":
            print("The {0} agrees to your friend request.".format(messagedata["target"]["nickName"]))
            return
        
        if messagedata["typeDescription"] == "TimerUpdatedEvent":
            conversation = json.loads(self.conversionservice.ConversationDetail(messagedata["conversationId"]).text)["value"]
            nikename = ""
            if conversation["requestUser"]["id"] != me["id"]:
                nikename = conversation["requestUser"]["nickName"]
            
            if conversation["targetUser"]["id"] != me["id"]:
                nikename = conversation["targetUser"]["nickName"]
            
            print("The {0} modified the message self-destruct time of your session with him. The current self-destruct time is {1}".format(
                nikename,
                second2time(messagedata["newTimer"])
            ))
            return
import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaConversationApiService(object):
    def __init__(self):
        self.apiaddress = KahlaApiAddressService()
        self.storagecookie = StorageCookieService()

    def SendMessage(self, conversationId, Message):
        r = requests.post("{0}/Conversation/SendMessage".format(self.apiaddress.getaddress()), 
                            data={
                                "Id": conversationId,
                                "Content": Message
                            },
                            cookies=self.storagecookie.get())
        
        return r

    def GetMesssages(self, conversationId, take):
        r = requests.get("{0}/Conversation/GetMessage?Id={1}&take={2}".format(self.apiaddress.getaddress(),
                                                                                str(conversationId), str(take)),
                                                                                cookies=self.storagecookie.get())

        return r
    
    def ConversationDetail(self, conversationid):
        r = requests.get("{0}/Conversation/ConversationDetail?id={1}".format(self.apiaddress.getaddress(), str(conversationid)), cookies=self.storagecookie.get())

        return r
import requests
import json
from Services.KahlaApiAddressService import KahlaApiAddressService
from Services.StorageCookieService import StorageCookieService

class KahlaConversationApiService(object):
    def __init__(self):
        self.apiaddress = KahlaApiAddressService()
        self.storagecookie = StorageCookieService()
    
    def ConversationDetail(self, conversationid):
        r = requests.get("{0}/Conversation/ConversationDetail?id={1}".format(self.apiaddress.getaddress(), str(conversationid)), cookies=self.storagecookie.get())

        return r

    
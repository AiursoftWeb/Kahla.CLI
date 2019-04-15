from Services.KahlaConversationApiService import KahlaConversationApiService
import json

class ProcessMessage(object):
    def __init__(self):
        self.conversionservice = KahlaConversationApiService()

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
        
        if message.find("[audio]") >= 0:
            audiokey = message.split("]")[1]
            message = "Audio | https://oss.aiursoft.com/download/fromkey/{0}".format(audiokey)
            return message

        return "Text | {0}".format(message)
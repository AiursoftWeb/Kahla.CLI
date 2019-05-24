from Services.KahlaConversationApiService import KahlaConversationApiService
import json

class ProcessMessage(object):
    def __init__(self):
        self.conversionservice = KahlaConversationApiService()

    def processMessage(self, message):
        if message.find("[img]") >= 0:
            message = message.split("]")[1].split("-")[0]
            message = "Photo | https://ossendpoint.azureedge.net/download/fromkey/{0}".format(message)
            return message
        
        if message.find("[video]") >= 0:
            message = message.split("]")[1]
            message = "Video | https://ossendpoint.azureedge.net/download/fromkey/{0}".format(message)
            return message

        if message.find("[file]") >= 0:
            data = message.split("]")[1].split("-")
            fileuri = self.conversionservice.FileDownloadAddress(data[0])
            fileuri = json.loads(fileuri.text)
            fileuri = fileuri["downloadPath"]
            message = "File | {2} | {0} | {1}".format(data[1], data[2], fileuri)
            return message
        
        if message.find("[audio]") >= 0:
            audiokey = message.split("]")[1]
            audiouri = self.conversionservice.FileDownloadAddress(audiokey)
            audiouri = json.loads(audiouri.text)
            audiouri = audiouri["downloadPath"]
            audiouri = audiouri.replace("audio", "audio.ogg")
            message = "Audio | {0}".format(audiouri)
            return message

        return "Text | {0}".format(message)

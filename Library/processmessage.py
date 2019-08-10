from Services.FileApiService import FileApiService
import json


class ProcessMessage(object):
    def __init__(self):
        self.fileservice = FileApiService()

    def processMessage(self, message):
        if message.find("[img]") >= 0:
            message = message.split("]")[1].split("|")[0]
            message = "Photo | https://probe.aiursoft.com/Download/InSites/{0}".format(
                message)
            return message

        if message.find("[video]") >= 0:
            message = message.split("]")[1]
            message = "Video | https://probe.aiursoft.com/Download/InSites/{0}".format(
                message)
            return message

        if message.find("[file]") >= 0:
            data = message.split("]")[1].split("|")
            fileuri = data[0]
            message = "File | https://probe.aiursoft.com/Download/InSites/{2} | {0} | {1}".format(
                data[1], data[2], fileuri)
            return message

        if message.find("[audio]") >= 0:
            audiouri = message.split("]")[1]
            message = "Audio | https://probe.aiursoft.com/Download/InSites/{0}".format(audiouri)
            return message

        return "Text | {0}".format(message)

from os import path
from os import mkdir

class HomeFloderConfig(object):
    def __init__(self):
        self.configpath = "{0}/.kahla".format(path.expanduser('~').replace("\\", "/"))
    
    def getconfigpath(self):
        return self.configpath

    def mkdirconfigpath(self):
        if path.exists(self.configpath) != True:
            mkdir(self.configpath)
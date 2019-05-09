import sys

class GetMessagesChecker(object):
    @staticmethod
    def Check(username, take):
        if username == None or take == None:
            print("usage: kahla getmessages [--username <username>] [--take 15]")
            print("simplified usage: kahla getmessages [-u <username>] [-t 15]")
            sys.exit(1)
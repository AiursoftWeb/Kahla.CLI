import sys


class SendChecker(object):
    @staticmethod
    def Check(username, message):
        if username is None or message is None:
            print(
                "usage: kahla send [--username <username>] [--message <message>]")
            print(
                "simplified usage: kahla send [-u <username>] [-m <message>]")
            sys.exit(1)

import sys


class DeleteFriendsChecker(object):

    @staticmethod
    def Check(username):
        if username is None:
            print("usage: kahla deletefriends [--username <username>]")
            print("simplified usage: kahla deletefriends [--u <username>]")
            sys.exit(1)

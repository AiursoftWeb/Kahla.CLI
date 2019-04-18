import sys

class SearchFriendsChecker(object):
    @staticmethod
    def Check(searchinput):
        if searchinput == None:
            print("usage: kahla searchfriends [--searchinput <username>]")
            print("simplified usage: kahla searchfriends [-si <username>]")
            sys.exit(1)
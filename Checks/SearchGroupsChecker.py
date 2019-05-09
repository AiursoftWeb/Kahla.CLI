import sys

class SearchGroupsChecker(object):
    @staticmethod
    def Check(searchinput):
        if searchinput == None:
            print("usage: kahla searchgroups [--searchinput <username>]")
            print("simplified usage: kahla searchgroups [-si <username>]")
            sys.exit(1)
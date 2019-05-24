import sys


class FriendsChecker(object):

    @staticmethod
    def Check(take):
        if take is None:
            print("usage: kahla friends [--take <take[not required]>]")
            print("simplified usage: kahla friends [-t <take[not required]>]")
            sys.exit(1)

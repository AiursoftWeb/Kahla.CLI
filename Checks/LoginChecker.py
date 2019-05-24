import sys


class LoginChecker(object):

    @staticmethod
    def Check(email, password):
        if email is None or password is None:
            print(
                "usage: kahla login [--email <username>] [--password <password>]")
            print(
                "simplified usage: kahla login [-e <username>] [-p <password>]")
            sys.exit(1)

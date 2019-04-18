import sys

class LoginChecker(object):

    @staticmethod
    def Check(email, password):
        if email == None or password == None:
            print("usage: kahla login [--email <username>] [--password <password>]")
            print("simplified usage: kahla login [-e <username>] [-p <password>]")
            sys.exit(1)
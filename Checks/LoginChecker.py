class LoginChecker(object):

    @staticmethod
    def Check(email, password):
        if email == None and password == None:
            print("usage: kahla login [--email <username>] [--password <password>]")
            print("simplified usage: kahla login [-e <username>] [-p <password>]")
            exit(1)
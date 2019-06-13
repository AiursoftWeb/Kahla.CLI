from Services.SignInStatusCheckService import SignInStatusCheckService

signinchecker = SignInStatusCheckService()

def loginchecker(func):
    def wrapper(*k):
        if signinchecker.check():
            return func(*k)
        else:
            print("You are not logged in!")
            exit(1)

    return wrapper
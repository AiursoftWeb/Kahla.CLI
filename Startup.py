from Controllers.HomeController import HomeController
from Controllers.LoginController import LoginController
from Controllers.UseStaggingController import UseStaggingController
from Controllers.UseMasterController import UseMasterController
from Controllers.LogoutController import LogoutController
from Controllers.FriendsController import FriendsController

class Startup(object):
	def __init__(self):
		pass
	
	@staticmethod
	def ConfigureRouting(routes):
		routes.add_command("home", HomeController())
		routes.add_command("usestagging", UseStaggingController())
		routes.add_command("usemaster", UseMasterController())
		routes.add_command("login", LoginController())
		routes.add_command("logout", LogoutController())
		routes.add_command("friends", FriendsController())
from Controllers.HomeController import HomeController
from Controllers.LoginController import LoginController
from Controllers.UseStaggingController import UseStaggingController
from Controllers.UseMasterController import UseMasterController
from Controllers.LogoutController import LogoutController
from Controllers.FriendsController import FriendsController
from Controllers.SearchFriendsController import SearchFriendsController
from Controllers.GetMessagesController import GetMessagesController
from Controllers.SendController import SendController

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
		routes.add_command("searchfriends", SearchFriendsController())
		routes.add_command("send", SendController())
		routes.add_command("getmessages", GetMessagesController())
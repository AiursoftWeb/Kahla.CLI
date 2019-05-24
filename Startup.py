from Controllers.LoginController import LoginController
from Controllers.LogoutController import LogoutController
from Controllers.FriendsController import FriendsController
from Controllers.SearchFriendsController import SearchFriendsController
from Controllers.GetMessagesController import GetMessagesController
from Controllers.SendController import SendController
from Controllers.DeleteFriendsController import DeleteFriendsController
from Controllers.LeaveGroupsController import LeaveGroupsController
from Controllers.GroupsController import GroupsController
from Controllers.SearchGroupsController import SearchGroupsController
from Controllers.ListenController import ListenController
from Controllers.VersionController import VersionController

class Startup(object):
    def __init__(self):
        pass
    
    @staticmethod
    def ConfigureRouting(routes):
        # kahla login
        routes.add_command("login", LoginController())
        # kahla logout
        routes.add_command("logout", LogoutController())
        # kahla friends
        routes.add_command("friends", FriendsController())
        # kahla searchfriends
        routes.add_command("searchfriends", SearchFriendsController())
        # kahla send
        routes.add_command("send", SendController())
        # kahla getmessages
        routes.add_command("getmessages", GetMessagesController())
        # kahla deletefriends
        routes.add_command("deletefriends", DeleteFriendsController())
        # kahla leavegroups
        routes.add_command("leavegroups", LeaveGroupsController())
        # kahla groups
        routes.add_command("groups", GroupsController())
        # kahla searchgroups
        routes.add_command("searchgroups", SearchGroupsController())
        # kahla listen
        routes.add_command("listen", ListenController())
        # kahla version
        routes.add_command("version", VersionController())
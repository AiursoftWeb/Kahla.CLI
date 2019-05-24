import sys


class LeaveGroupsChecker(object):
    @staticmethod
    def Check(group):
        if group is None:
            print("usage: kahla leavegroups [--group <groupname>]")
            print("simplified usage: kahla leavegroups [-g <groupname>]")
            sys.exit(1)

import GlobalConfigs

def Version(data):
    print("Current Kahla Version is: {0}".format(data["version"]))
    print("Local Kahla Version is {0}".format(GlobalConfigs.CurrentVersion))
    if data["version"] == GlobalConfigs.CurrentVersion:
        print("You're running the latest Kahla CLI.")
    else:
        print("You're running an old Kahla CLI.")
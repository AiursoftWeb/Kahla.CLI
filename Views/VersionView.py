def Version(data):
    print("Current Kahla Version is: {0}".format(data["version"]))

    if data["latestVersion"] == data["version"]:
        print("Kahla CLI is the latest version")
    else:
        print("Your Kahla CLI is not the latest version")

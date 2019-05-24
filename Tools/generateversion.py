import json

with open("./package.json", "r") as f:
    data = json.loads(f.read())
    with open("./package.py", "w") as fw:
        fw.write("version = '{0}';stable = {1}".format(data["version"], data["stable"]))
#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from Startup import Startup
from Services.HomeFloderConfig import HomeFloderConfig

app = Flask(__name__)
manager = Manager(app)
configpath = HomeFloderConfig()

def main():
    # Seed Config Path
    configpath.mkdirconfigpath()
    # Configure Routing
    Startup.ConfigureRouting(manager)
    # Start Application
    manager.run()

if __name__ == "__main__":
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_script import Command
from Startup import Startup
from platform import system

app = Flask(__name__)
manager = Manager(app)

# Configure Routing
Startup.ConfigureRouting(manager)

if __name__ == "__main__":
    manager.run()
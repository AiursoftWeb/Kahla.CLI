from flask_script import Command
from importlib import import_module

class Controller(Command):
    def compute(self, *k):
        conrollername = self.__class__.__name__.split("Controller")[0]
        result = self.main(*k)
        module = import_module("Views.{}".format("{}View".format(conrollername)))
        eval("module.{}(result)".format(conrollername))

    def main(self):
        pass
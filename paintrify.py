#!/usr/bin/python3
"""
Paintrify
"""
__author__ = "Marek Sedlacek"
__date__ = "August 2022"
__version__ = "0.0.1"
__email__ = "mr.mareksedlacek@gmail.com"

from xmlrpc.client import boolean
import PyQt5
import sys
import argparse
import gui
import generator
import webbrowser
import json
from PyQt5.QtWidgets import QApplication

DEBUG = False

def info(msg):
    """
    Debug print
    """
    if DEBUG:
        print("INFO: {}.".format(msg), file=sys.stderr)
    return


class Paintrify:
    """
    Main program class
    """

    def __init__(self, argparser):
        """
        Constructor
        """
        self.argparser = argparser
        self.add_args(argparser)
        self.argopts = self.argparser.parse_args()

        self.config = generator.Config(self.argopts)

        # GUI
        self.window = gui.GUI(self.config, self.argparser, info)
        

    def add_args(self, argparser):
        """
        Adds arguments to the argparser
        """

        


if __name__ == "__main__":
    DEBUG = True  # TODO: Move to args

    # Get debug option
    argparser = argparse.ArgumentParser(description="Paintrify.")
    argparser.add_argument("--debug", default=False, action="store_const",
                            dest="debug", const=True,
                            help="Debugging messages.")
    _args = argparser.parse_args()
    DEBUG = _args.debug

    info("Debug prints ON")

    main_app = QApplication(sys.argv)
    app = Paintrify(argparser)
    sys.exit(main_app.exec_())
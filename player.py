__author__ = "wmyers559"

import entity

class Player(object):
    """ """

    def __init__(self, health):
        self.location = ""  # Not sure what this should be
        self.health = health
        self.inventory = {}
        self.equiptment = {}
        self.stats = {}

    def grab(self, item):
        pass

    def move(self, direction):
        pass

    def examine(self, subject):
        pass

    def use(self, item1, item2):
        pass

    def open(self, item):
        pass

    

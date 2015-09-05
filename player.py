__author__ = "wmyers559"

import entity
import error

class Player(entity):
    """Basic player object. Takes initial health as a argument."""

    def __init__(self, health):
        self.location = ""  # Not sure what this should be yet
        self.health = health
        self.inventory = {}
        self.equiptment = {}
        self.stats = {}

    def grab(self, item):
        pass

    def move(self, direction):
        pass

    def examine(self, subject):
    """Get the description of an object."""
        print(subject.description_verbose)

    def use(self, item1, item2):
        pass

    def open(self, item):
    """Checks to see if an object is openable and then tries to open it."""
        if (item.openable == True)
            print(item.#Whatever we want to name the method.)

        else
            raise Exception("Invalid keyword")

    def interact(self, item):
        #item.action()  Maybe??
        pass

    def damage(self, damage):
    """Subtracts the amount of damage(@param damage) done from the health of the player."""
        self.health -= damage


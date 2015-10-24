"""

@author 'jim'
"""
from prototypes.traits import Traits
from prototypes.moretraits import MoreTraits


class Character(Traits, MoreTraits):

    def __init__(self, name):
        self.name = name

    def talk(self):
        print("My name is {}".format(self.name))

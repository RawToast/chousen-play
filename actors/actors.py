"""

@author 'jim'
"""


class Character(object):
    def __init__(self, name):
        self.name = name

        self.health = 100
        self.max_health = 100
        self.speed = 100
        self.turn_count = 0

    def wait_for_turn(self):
        # print("{} is waiting, current count {}".format(self.name, self.turn_count))
        self.turn_count = self.turn_count + self.speed

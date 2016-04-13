"""
Dummy server for now
@author 'jim'
"""
from copy import copy


class ChousenServer:
    """
    Fake server implementation, simply to separate the code.
    """

    def start_game(self):
        run = True
        while run:
            decide_turn(context)

            take_turn(context)

            end_turn(context)

        Output.send("Game has ended")


    def handle_command(self, command, character):
        success = False
        result = "{}"
        if command.lower() in COMMANDS.keys():
            _command = COMMANDS.get(command.lower())
            success, result = _command(self, character)
        return success, result

    def wait(self, character):
        print("Wait command received for {}".format(character.name))
        return True, "{} waits".format(character.name)


COMMANDS = {"wait": ChousenServer.wait,

            }


# Needs to move to server
class GameState(object):
    __turn = 1

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def increment_turn(self):
        self.__turn += 1
        return copy(self.__turn)

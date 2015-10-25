"""

@author 'rawtoast'
"""
from copy import copy
from actors import Character
from client.output import Output

_input = input("Player 1 what is your name? ")
_player1 = Character(name=_input)
# Experiment!
_player1.speed = 150

_input = input("Player 2 what is your name? ")
_nextPlayer = Character(name=_input)


class GameState(object):
    __turn = 1

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def increment_turn(self):
        self.__turn += 1
        return copy(self.__turn)


_gameState = GameState(_player1, _nextPlayer)


def decide_turn(context):
    threshold = 1000

    player1 = context.player1
    player2 = context.player2

    _players = [player1, player2]

    def has_reached_threshold(turn_count):
        return turn_count >= threshold

    reached_threshold = []

    # Refactor this section
    while not reached_threshold:
        reached_threshold = [x for x in _players if has_reached_threshold(x.turn_count)]

        if not reached_threshold:
            for _player in _players:
                _player.wait_for_turn()

        if reached_threshold:
            _top = reached_threshold[0]
            if len(reached_threshold) > 1:
                _max = 0

                for _player in reached_threshold:
                    if _player.turn_count > _max:
                        _max = _player.turn_count
                        _top = _player

            print("Current turn given to {} turn_count was {}".format(_top.name,
                                                                      _top.turn_count))
            context.current_player = _top
            context.current_player.turn_count = 0


def take_turn(context):
    player = context.current_player
    Output.send("It is {}'s turn".format(player.name))
    _input = input("Command? ")
    print("Input was: {}".format(player.name, _input))



def end_turn(context):
    Output.send("Turn {} finished".format(context.increment_turn()))


def start_game(context):
    run = True
    while run:
        decide_turn(context)

        take_turn(context)

        end_turn(context)

    Output.send("Game has ended")


start_game(_gameState)

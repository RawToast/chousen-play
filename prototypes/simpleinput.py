"""
Playing with user input
@author 'rawtoast'
"""
from prototypes import Character

_input = input("What is your name? ")

you = Character(_input)

you.talk()
you.shout_about_it()
you.whisper_about_it()

# Static mixin
Character.shout_about_it()

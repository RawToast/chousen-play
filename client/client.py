"""

@author 'rawtoast'
"""
from server.server import ChousenServer


class Client:
    __shared_state = {}

    __server = None

    def __init__(self):
        self.__dict__ = self.__shared_state
        self._server = ChousenServer()

    def send_command(self, data, player):
        return self.__send_command_to_server(data, player)

    def __send_command_to_server(self, data, player):
        return self._server.handle_command(data, player)

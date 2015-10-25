"""

@author 'rawtoast'
"""


class Client:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    @staticmethod
    def send_command(data):
        if data == "fail":
            return False, data
        return True, data

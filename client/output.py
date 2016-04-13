"""

@author 'rawtoast'
"""


class Output:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    @staticmethod
    def send(data):
        print(data)

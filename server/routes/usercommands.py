"""
Entry point for user commands. Not a great class/filename
@author 'rawtoast'
"""
from tornado.web import RequestHandler
from tornado.escape import json_decode
from http import HTTPStatus
from server.util.routedecorator import Route
from server.util.constants import TOKEN, COMMAND, WAIT, ATTACK

# {
#   "token": "123123124",
#   "command" : "WAIT"
# }

class ServerCommands(RequestHandler):

    @Route('/command/input/')
    def post(self):
        data_json = json_decode(self.request.body)
        print("Received request with body {}".format())

        if self._ensure_command_from_active_player(data_json) and
            self._ensure_command_is_valid(data_json):


            self.set_status(HTTPStatus.OK)
        self.finish()


    def _ensure_command_from_active_player(self, data_json):
        _token = data_json.get(TOKEN)

        if False:
            print("Request sent from non-active user")
            self.set_status(HTTPStatus.BAD_REQUEST)
            return False
        return True

    def _ensure_command_is_valid(self, data_json):
        _command = data_json.get(COMMAND)
        valid = True

        if _command not in [WAIT, ATTACK]:
            print("Request sent with invalid command")
            valid = False

        if not valid:
            self.set_status(HTTPStatus.BAD_REQUEST)

        return valid
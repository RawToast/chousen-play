"""
Entry point for user commands. Not a great class/filename
@author 'rawtoast'
"""
from tornado.web import RequestHandler
from tornado_utils.routes import route
from tornado.escape import json_decode
from http import HTTPStatus


class ServerCommands(RequestHandler):
    @route('/command/input/')
    def post(self):
        data_json = json_decode(self.request.body)

        print("Received request with body {}".format())

        self.set_status(HTTPStatus.OK)
        self.finish()

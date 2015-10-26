"""
Dummy server for now
@author 'jim'
"""


class ChousenServer:
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

"""
Chosen server application. This will start the server
@author 'rawtoast'
"""
import tornado.web
from gameserver.routes.usercommands import ServerCommands
from gameserver.util.routedecorator import Route

ServerCommands

app = tornado.web.Application(Route.get_routes())

#handlers = [
 #           (r"/all_book/", ServerCommands)
  #      ]

#app = tornado.web.Application.__init__(handlers)



if __name__ == "__main__":
    port = 8888
    app.listen(port)
    print("Starting tornado instance on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()

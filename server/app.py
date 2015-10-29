"""
Chosen server application. This will start the server
@author 'rawtoast'
"""
import tornado.web
from tornado_utils.routes import route

app = tornado.web.Application(route.get_routes())

if __name__ == "__main__":
    port = 8888
    app.listen(port)
    print("Starting tornado instance on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()

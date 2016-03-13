import tornado.ioloop
import tornado.web
import tornado.httpserver
from urls import url_patterns
from settings import settings


class TornadoCreateApp(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,url_patterns,**settings)
#
def make_app():
    return tornado.web.Application(url_patterns)

if __name__ == "__main__":
    app = TornadoCreateApp()
    # http_server = tornado.httpserver.HTTPServer(app)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
import tornado.web

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
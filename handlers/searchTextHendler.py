import tornado.web
import json
class searchTextHendler(tornado.web.RequestHandler):
    def get(self,text):
        print text
        self.write(text)
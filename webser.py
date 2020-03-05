import tornado.ioloop
import tornado.web
from evaluators import dict_of_op

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        op = self.get_argument('op', None)
        try:
            x = int(self.get_argument('x', None))
            y = int(self.get_argument('y', None))
            try:
                op = dict_of_op[op]
                result = str(op.eval(x, y))
                self.write(result)
            except KeyError:
                self.write("Wrong operation")
        except ValueError:
            self.write("ERRRRRRRROR")








if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/get", GetHandler),
    ])
    application.listen(8889)
    tornado.ioloop.IOLoop.current().start()



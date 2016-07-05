import sys

import tornado.ioloop
import tornado.web

from tornado_example import settings
from tornado_example.data_access_layer import DataAccessLayer
from tornado_example.routes import RoutesManager


def make_app():
    return tornado.web.Application(RoutesManager(DataAccessLayer).get_url_patterns(), **settings.TORNADO_SETTINGS)

def main():
    app = make_app()
    app.listen(sys.argv[1])  # Getting port number to listen to as an argument
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
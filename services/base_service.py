from tornado import web


class BaseService(object):
    """
    BaseService is an abstract class which represents a service in the API.
    Each service is a subclass of this class, and usually add some additional routes (handlers)
    to the basic routes each service has. Furthermore, each service needs to define its
    logic_class and logic_class_stub classes
    """
    base_handlers = (
        # Here you can put some generic handlers for the use of all services
    )
    handlers = []
    logic_class = None

    def __init__(self, service_name, data_layer):
        if self.logic_class is None or self.logic_class_stub is None:
            raise NotImplementedError()

        self.service_name = service_name
        self.data_layer = data_layer
        self.base_routes = [self.generate_url(handler[1], handler[0]) for handler in self.base_handlers]
        self.urls = [self.generate_url(handler[1], handler[0]) for handler in self.handlers]

    def routes(self):
        return self.urls + self.base_routes

    def get_logic_layer(self):
        return self.logic_class(self.data_layer)

    def generate_url(self, handler, route):
        kwargs = {'logic_layer': self.get_logic_layer(), 'service_name': self.service_name}
        return web.url(r'/' + self.service_name + route, handler, kwargs=kwargs)
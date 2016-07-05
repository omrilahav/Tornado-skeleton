from tornado_example.services.example_service.example_service import ExampleService
from tornado_example.websocket_handler.example_websocket import websockets_routes


class RoutesManager(object):
    def __init__(self, data_layer_class):
        self.data_layer_class = data_layer_class

    def get_url_patterns(self):
        self.data_layer = self.data_layer_class()

        services = [
            ExampleService("Example", self.data_layer),
        ]

        routes_lists = [service.routes() for service in services]
        routes = []
        for routes_list in routes_lists:
            routes.extend(routes_list)

        routes += websockets_routes(self.data_layer)

        return routes
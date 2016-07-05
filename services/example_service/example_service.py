import json

from tornado_example.services.base_handler import BaseHandler
from tornado_example.services.base_service import BaseService
from tornado_example.services.example_service.example_logic import ExampleLogic


class ExampleHandler(BaseHandler):
    def get(self):
        data = self.logic_layer.get()

        self.write(json.dumps({
            "data": data
        }))


class ExampleByIDHandler(BaseHandler):
    def get(self, id):
        entity = self.logic_layer.get_by_id(id)

        self.write(json.dumps({
            "entity": entity
        }))


class ExampleService(BaseService):
    handlers = (
        ('/', ExampleHandler),
        ('/([0-9a-zA-Z_\-]+)', ExampleByIDHandler)
    )
    logic_class = ExampleLogic
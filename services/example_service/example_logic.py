from tornado_example.services.base_logic import BaseLogicAbstract


class ExampleLogic(BaseLogicAbstract):
    def __init__(self, data_layer):
        super(ExampleLogic, self).__init__(data_layer)

    def get(self):
        return None
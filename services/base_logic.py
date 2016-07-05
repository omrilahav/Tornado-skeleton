class EntityNotExistsException(Exception):
    pass

class BaseLogic(object):
    """
    Every service should have its own logic. The logic class is between the service to the
    data layer. The logic layer is actually the business layer of the application, and is responsible
    for the data manipulation.
    """
    def __init__(self):
        pass

    def get_all(self):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def get_by_id(self, id):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class BaseLogicAbstract(BaseLogic):
    """
    This abstract class is the base class for all the services which its data is being handled by oracle database.
    """
    def __init__(self, data_layer):
        super(BaseLogicAbstract, self).__init__()
        self.data_layer = data_layer

    def get(self):
        return None

    def get_all(self):
        return None

    def get_by_id(self, id):
        return None

    def count(self):
        return 0
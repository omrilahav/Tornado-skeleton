class DataAccessLayer(object):
    """
    This class is responsible for creating connections to different databases and return it to caller handlers.
    It works in a lazy manner, means that the initial connection to the databases is occur only after first request
    to data from that database. This way the connection requests are coming from the services, and not from the
    Tornado application - which means that the application works great even if some of the databases has problems.
    The services will handle connection errors.
    """
    def __init__(self):
        pass

    def get_some_data(self):
        pass
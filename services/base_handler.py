import json
import tornado.web
from tornado_cors import CorsMixin

class BaseHandler(CorsMixin, tornado.web.RequestHandler):
    """
    This is an abstract class that represents the handlers. Every service can
    have multiple handlers, where each handler is an API endpoint (has its own route),
    and implements at least one of the functions: get, post, put, delete (see Tornado Docs for details)
    """
    def initialize(self, logic_layer, service_name):
        self.service_name = service_name
        self.logic_layer = logic_layer

    CORS_ORIGIN = '*'

    # Value for the Access-Control-Allow-Headers header.
    # Default: None (no header).
    CORS_HEADERS = 'Content-Type, Authorization'

    # Value for the Access-Control-Allow-Methods header.
    # Default: Methods defined in handler class.
    # None means no header.
    CORS_METHODS = 'POST'

    # Value for the Access-Control-Allow-Credentials header.
    # Default: None (no header).
    # None means no header.
    CORS_CREDENTIALS = True

    # Value for the Access-Control-Max-Age header.
    # Default: 86400.
    # None means no header.
    CORS_MAX_AGE = 21600

    # Value for the Access-Control-Expose-Headers header.
    # Default: None
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'

    def data_received(self, chunk):
        raise NotImplementedError()

    def write_error(self, status_code, **kwargs):
        self.write("Write some error description which will be sent to the front side")

    def get_input(self, var_name, var_type):
            return var_type(self.get_arguments(var_name)[0]) if len(self.get_arguments(var_name)) == 1 else None

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.
        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                raise tornado.web.HTTPError(400, msg)
            return default
        arg = self.request.arguments[name]
        return arg

    def _handle_request_exception(self, e):
        """
        Handle all exceptions that rises from the handlers that will inherit this class.
        Comment out this method if you want the exceptions to stop execution where it raises for debug.
        :param e: Exception
        :return:
        """
        pass
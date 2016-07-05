from tornado import web, websocket


def websockets_routes(data_layer):
    module_name = 'WebSocket'
    return [
        web.url(r'/' + module_name + '/Echo', EchoWebSocket),
    ]

clients = []


class EchoWebSocket(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")
        if self not in clients:
            clients.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        if self in clients:
            clients.remove(self)
        print("WebSocket closed")
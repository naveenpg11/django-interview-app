from . import consumers
from channels import route
from .consumers import ws_connect, ws_receive, ws_disconnect

channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,

}
   
#custom_routing = [
    #route("chat.receive", chat_join, command="^join$"),
#]



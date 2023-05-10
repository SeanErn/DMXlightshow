import tornado.web
import tornado.websocket
import tornado.ioloop
import WS.GET as wsGET
import WS.SET as wsSET
import json
import WS.status as wsStatus
import Control.sceneHandler as sceneHandler

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True # allow all origins
    
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print(message)
        response = self.handle_request(message)
        self.write_message(response)
        
    def on_close(self):
        print("WebSocket closed")

    def handle_request(self, message):
        try:
            type = json.loads(message)["type"]
            print(type)
        except:
            return wsStatus.failedParseRequest()
        # Use a case statement to handle different requests
        if type == "startScene":
            sceneHandler.startScene(json.loads(message)["data"]["sceneName"])
        else:
            return wsStatus.failedParseType()

def make_app():
    return tornado.web.Application([
        (r"/", WebSocketHandler),
    ])
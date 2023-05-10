import WS.WShandler as WS
import tornado.ioloop

# Construct WS app and listen on port 5000
if __name__ == "__main__":
    app = WS.make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()

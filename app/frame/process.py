from frame.server import server

class Process:
    def __init__(self, typ, bp):
        self.typ = typ
        self.bp = bp


    def start(self):
        from frame.zk import zk
        zk.start()
        server.start(self.typ, 1)

        from frame.flask_app import app as flask_app
        flask_app.register_blueprint(self.bp)
        flask_app.run(port=8000)


    # def register_module(self):
    #     pass
    #
    #
    # def init(self):
    #     return self

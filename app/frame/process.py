from frame.router import router

class Process:
    def __init__(self, typ, bp):
        self.typ = typ
        self.bp = bp


    def start(self):
        from frame.zk import zk
        zk.start()
        router.init(self.typ, 1)

        from frame.http_server import app as flask_app
        flask_app.register_blueprint(self.bp)
        flask_app.run(port=8000)



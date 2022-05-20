class HandlerManager(object):
    """"""

    def __init__(self):
        """"""
        self.m = {}


    def register(self, uri, func):
        self.m[uri] = func
        return self
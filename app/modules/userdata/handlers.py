from frame.handler import HandlerManager


def handle_create(ctx):
    pass






handlerManager = HandlerManager()
handlerManager.register("user/create", handle_create)



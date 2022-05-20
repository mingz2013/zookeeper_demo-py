class ProcessType:
    Util = "util"
    Gateway = "gateway"
    Mgr = "mgr"


def get_process(typ):
    if typ == ProcessType.Mgr:
        from .mgr import bp
    elif typ == ProcessType.Util:
        from .util import bp
    elif typ == ProcessType.Gateway:
        from .gateway import bp
    else:
        raise Exception("type err")
    from frame.process import Process

    return Process(typ, bp)

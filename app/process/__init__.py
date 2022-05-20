class ProcessType:
    Util = "util"
    Gateway = "gateway"
    Mgr = "mgr"


def get_process(typ):
    if typ == ProcessType.Mgr:
        from .mgr import process
    elif typ == ProcessType.Util:
        from .util import process
    elif typ == ProcessType.Gateway:
        from .gateway import process
    else:
        raise Exception("type err")

    return process

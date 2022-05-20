from kazoo.client import KazooClient
from kazoo.client import KazooState, KeeperState

zk = KazooClient(hosts='127.0.0.1:2181')

@zk.add_listener
def zk_listener(self, state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        print("on_listen lost")
        pass
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        print("on_listen suspended")
        pass
    elif state == KazooState.CONNECTED:
        print("on_listen connected")
        if self._zk.client_state == KeeperState.CONNECTED_RO:
            print("Read only mode!")
        else:
            print("Read/Write mode!")
        pass

    else:
        # Handle being connected/reconnected to Zookeeper
        print("on_listen state:", state)
        pass


@zk.ChildrenWatch("/my/favorite/node")
def watch_children(children):
    print("Children are now: %s" % children)
# Above function called immediately, and from then on


@zk.DataWatch("/my/favorite")
def watch_node(data, stat):
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))




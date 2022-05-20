from kazoo.client import KazooClient
from kazoo.client import KazooState, KeeperState


class ZkWrapper(object):
    def __init__(self, host="localhost:2181"):
        self.host = host
        self._zk = KazooClient(hosts='127.0.0.1:2181')
        self._zk.add_listener(self._on_listen)

    def start(self):
        self._zk.start()

    def stop(self):
        self._zk.stop()

    def _on_listen(self, state):
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


    def ensure_path(self, path, acl=None):
        """#将递归地创建节点和沿途所需路径中的任何节点，但不能为节点设置数据，只能设置ACL。"""
        self._zk.ensure_path(path, acl)

    def create(self, path, value=b"", acl=None, ephemeral=False,
               sequence=False, makepath=False, include_data=False):
        """# 创建一个节点，并可以在节点上设置数据以及监视功能。它要求它的路径首先存在，除非makepath选项设置为True。"""
        self._zk.create(path, value, acl, ephemeral, sequence, makepath, include_data)


    def exists(self, path, watch=None):
        return self._zk.exists(path, watch)


    def get(self, path, watch=None):
        return self._zk.get(path, watch)

    def get_children(self, path, watch=None, include_data=False):
        return self._zk.get_children(path, watch, include_data)


    def set(self):
        """# 设置数据"""
        pass

    def delete(self):
        """# 删除数据"""
        pass

    def retry(self):
        """重试"""
        pass

    def watch(self, path, my_func):
        """监听，可以在get，exists，get_children等方法watch参数传入函数，也可以使用装饰器"""
        self.get(path, my_func)
        pass

    def transaction(self):
        """原子操作"""
        transaction = self._zk.transaction()
        transaction.check('/node/a', version=3)
        transaction.create('/node/b', b"a value")
        results = transaction.commit()
        return results


    def start_async(self):
        pass

    def create_async(self):
        # 增删改查等都有异步操作
        pass




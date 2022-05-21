import zk


class Conf(object):
    def __init__(self):
        """"""
        self.name = ""
        self.id = 0
        self.conf_server_list_cache = None
        self.conf_game_config = None


    def init(self,  name, id_):
        self.name = name
        self.id = id_
        self.register_self()
        self.get_conf()
        pass


    def register_self(self):
        """注册节点, 临时节点"""
        zk.zk.create(f"/server/{self.name}/{self.id}", ephemeral=True, makepath=True)


    # @zk.zk.ChildrenWatch("/server/")
    def watch_server_list(self, children):
        """监听服务器列表变动"""
        self.conf_server_list_cache = children

    def get_conf(self):
        self.conf_server_list_cache = zk.zk.get_children("/server/", self.watch_server_list)
        self.conf_game_config = zk.zk.get_children("/game_config/", self.watch_game_config)

    def watch_game_config(self, children):
        """
        监听业务配置变动
        :param children:
        :return:
        """
        self.conf_game_config = children


    def select_host(self, hash_index):
        pass
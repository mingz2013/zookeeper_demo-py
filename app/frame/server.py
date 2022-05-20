import json

import requests

import zk


class Server(object):
    def __init__(self):
        self.name = ""
        self.id = 0
        self.conf_server_list_cache = None
        self.conf_game_config = None

        pass

    def start(self, name, id_):
        self.name, self.id = name, id_
        self.init()
        pass

    def init(self):
        self.register_self()
        self.get_conf()
        pass

    def register_self(self):
        """注册节点"""
        zk.zk.ensure_path(f"/server/{self.name}/{self.id}")  # , acl=100)
        # TODO 启动一个循环，用来在过期前自动注册

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

    def select_server_host(self, hash_index):
        """一致性hash算法，选择一个server返回"""
        return self.conf_server_list_cache[hash_index]

    def call_api(self, url, msg):
        """
        目前用http，后续可换成tcp，或消息队列
        :param host:
        :param msg:
        :return:
        """

        resp = requests.post(url, data=msg)
        return json.loads(resp.content)

    def call_rpc(self, hash_index, msg):
        host = self.select_server_host(hash_index)
        url = f"{host}/call_rpc/"
        return self.call_api(url, msg)

    

    def send_msg(self, hash_index, msg):
        host = self.select_server_host(hash_index)
        url = f"{host}/send_msg"
        self.call_api(url, msg)


server = Server()

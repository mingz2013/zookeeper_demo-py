import json

import requests


from frame.conf import Conf

class Router(object):
    def __init__(self):
        self.name = ""
        self.id = 0
        self.conf = Conf()
        pass

    def init(self, name, id_):
        self.name, self.id = name, id_
        self.conf.init(self.name, self.id)


    def select_server_host(self, hash_index):
        """一致性hash算法，选择一个server返回"""
        return self.conf.conf_server_list_cache[hash_index]

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


router = Router()

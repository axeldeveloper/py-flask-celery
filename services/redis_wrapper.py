import os

import redis


class RedisWrapper(object):

    def __init__(self):
        self.host = os.environ.get('REDIS_HOST')
        self.port = os.environ.get('REDIS_PORT')
        self.db = os.environ.get('REDIS_DB')
        self.pwd = os.environ.get('REDIS_PWD')
        self.usr = os.environ.get('REDIS_USR')
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.pwd)

    def local_connect(self,):
        connection_pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)
        return redis.StrictRedis(connection_pool=connection_pool)

    def sever_connect(self):
        return redis.Redis(connection_pool = self.pool)

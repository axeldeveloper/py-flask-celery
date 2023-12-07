import json
import unittest
import redis

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = "redis-17684.c274.us-east-1-3.ec2.cloud.redislabs.com"
        uss = "default"
        pwd = "IORXfdjQJAuMqwloFiBCWVsFhgW3Oj5I"
        rc = redis.Redis(host='localhost', port=6379, db=0)
        # redis_pool = redis.ConnectionPool(host=url, port=17684, username=uss, password=pwd, db=0)

        rc.set('foo', 'bar')
        # True

        a = rc.get('foo')
        assert a is not None  # add assertion here

    def test_local(self):
        url = "redis-17684.c274.us-east-1-3.ec2.cloud.redislabs.com"
        uss = "default"
        pwd = "IORXfdjQJAuMqwloFiBCWVsFhgW3Oj5I"
        # redis_pool = redis.Redis(host='localhost', port=6379, db=0)
        # redis_pool = redis.ConnectionPool(host=url, port=17684, username=uss, password=pwd, db=0)
        # rc = redis.StrictRedis(connection_pool=redis_pool)
        rc = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        rc.set('test', 'ConnectionPool')

        #
        # personal_information = {
        #     'name': 'Rahul',
        #     'age': 20,
        #     'address': {
        #         'house_no': 189,
        #         'flat_name': 'Golden Flower',
        #         'area': 'Guindy'
        #     },
        #     'languages_known': ['english', 'hindi', 'tamil']
        # }
        # rc.set('personal_information', json.dumps(personal_information))
        # True
        a = rc.get('test')
        assert a is not None

if __name__ == '__main__':
    unittest.main()
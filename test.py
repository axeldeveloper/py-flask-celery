import unittest

import redis


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         url = "redis-17684.c274.us-east-1-3.ec2.cloud.redislabs.com"
#         rc = redis.Redis(
#             host=url,
#             port=17684,
#             username="default",
#             password="IORXfdjQJAuMqwloFiBCWVsFhgW3Oj5I",
#             decode_responses=True
#         )
#         rc.set('foo', 'bar')
#         # True
#
#         rc.get('foo')
#         self.assertEqual(True, True)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()


def calls():
    import redis
    rc = redis.Redis(
        host='XXXXXX.redislabs.com',
        port=17684,
        password='CXXXXXXXX',
        ssl=False,
    )
    rc.set('foo', 'bar')
    # True

    rc.get('foo')

def something():
    url = "XXXXXX.redislabs.com"
    rc = redis.Redis(
        host=url,
        port=17684,
        username="default",
        password="CXXXXXXXX",
        decode_responses=True
    )
    rc.set('foo', 'bar')
    # True

    rc.get('foo')
    print("fimmmm")

if __name__ == '__main__':
     calls()
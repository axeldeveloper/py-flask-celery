import os
from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'a2%mnuo4p+i3v=yr&x2@l(fnbbn4o3az8nep$fyu^k1ljnj'
    DATABASE_URL = "postgresql://postgres:postgres@localhost/mss_pg_db"
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    # BROKER_URL = 'redis://localhost:6379/0'
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
    CELERY_ACCEPT_CONTENT = ['json', 'yaml'] # ['application/json']
    # CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('tasks',)
    CELERY_WORKER_HIJACK_ROOT_LOGGER = False

    # redis
    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = 6379
    REDIS_DB = 0



class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

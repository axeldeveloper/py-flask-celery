import os
from dotenv import load_dotenv
from kombu import Queue, Exchange

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'a2%mnuo4p+i3v=yr&x2@l(fnbbn4o3az8nep$fyu^k1ljnj'
    # DATABASE_URL = "postgresql://postgres:postgres@localhost/mss_pg_db"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = DATABASE_URL
    # BROKER_URL = 'redis://localhost:6379/0'
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    # CELERY_ACCEPT_CONTENT = ['json', 'yaml'] # ['application/json']
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('tasks',)
    CELERY_BROKER_HEARTBEAT = 0
    CELERY_BROKER_POOL_LIMIT = 1
    CELERY_BROKER_CONNECTION_TIMEOUT = 10
    CELERY_WORKER_HIJACK_ROOT_LOGGER = False
    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_TASK_TRACK_STARTED = True
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'
    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
    )
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


class FBSetting:
    GFB_CONFIG = {
        "type": os.environ.get("SERVICE_ACCOUNT"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id":  os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
    }

class CeleryConfig:
    # CELERY_IMPORTS = ('proj.tasks')
    CELERY_RESULT_EXTENDED = True
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_ACCEPT_CONTENT = ['application/json', 'json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json' 
    # CELERY_TIMEZONE = 'Asia/Seoul'
    CELERY_ENABLE_UTC = False
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/0')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    REDIS_HOST = 'localhost'
    REDIS_PASSWORD = ''
    REDIS_PORT = 6379
    REDIS_URL =  os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
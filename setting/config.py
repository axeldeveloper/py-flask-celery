import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #DATABASE_URL = "postgresql://mss:mss766312@postgresql-mss.alwaysdata.net/mss_pg_db"
    DATABASE_URL = "postgresql://postgres:postgres@localhost/mss_pg_db"
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    # CELERY_ACCEPT_CONTENT = ['application/json']

    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
    CELERY_ACCEPT_CONTENT = ['json', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('tasks',)
    CELERY_WORKER_HIJACK_ROOT_LOGGER = False


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

from celery.schedules import crontab

from route.api_worker import wrk
from setting.config import DevelopmentConfig
from models.database import db
from flask_migrate import Migrate
from celery import Celery
import os

migrate = Migrate()

BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
DATABASE_URL = os.environ.get('DATABASE_URL')


class CeleryConfig:
    # CELERY_IMPORTS = ('proj.tasks')
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Seoul'
    CELERY_ENABLE_UTC = False


CELERYBEAT_SCHEDULE = {
    'db_connect_things': {
        'task': 'application.lib.tasks.db_connect_things',
        'schedule': crontab(minute=0, hour='*/12'),
    }
}


def init_celery3(app):
    celery = Celery(
        app.import_name,
        broker=BROKER_URL,
        backend=RESULT_BACKEND,
        result_extended=True,
        config_source=app.config
    )

    # celery.config_from_object(app.config)
    # celery.conf.update(app.config)
    # celery.conf.update(CELERYBEAT_SCHEDULE)
    class ContextTask(celery.Task):
        # abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                # return TaskBase.__call__(self, *args, **kwargs)
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    # celery.config_from_object(CeleryConfig)
    # celery.conf.update(app.config)
    return celery


def init_celery(app):
    celery = Celery(
        app.import_name,
        broker=BROKER_URL,
        backend=RESULT_BACKEND,
        result_extended=True,
        # config_sourc=app.config
    )

    # celery.config_from_object(app.config)
    # celery.conf.update(app.config)
    # celery.conf.update(CELERYBEAT_SCHEDULE)
    # TaskBase = celery.Task
    class ContextTask(celery.Task):
        # abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                # return TaskBase.__call__(self, *args, **kwargs)
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    # celery.config_from_object(CeleryConfig)
    # celery.conf.update(app.config)
    return celery


def register_blueprint(app):
    # from proj.api import users
    # app.register_blueprint(users.user_bp, url_prefix='/user')
    return app


def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['CELERYBEAT_SCHEDULE'] = {}
    celery_app = init_celery(app)
    # celery_app.conf.update(CeleryConfig)
    with app.app_context():
        db.init_app(app)
    # db.init_app(app)
    migrate.init_app(app, db)
    # migrate = Migrate(app, db)
    app.register_blueprint(wrk, url_prefix='/task/')
    return app, celery_app

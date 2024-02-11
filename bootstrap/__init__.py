import os

from celery.schedules import crontab
from flask import Flask
from flask_restful import Api
from models.all_type import AllTypes

from route.api_all_type import ApiAllType, ApiAllTypeParam
from route.api_fifo import ApiFifo, ApiFifoConsumer
from route.api_worker import wrk
from setting.config import DevelopmentConfig
from models.database import db
from flask_migrate import Migrate
from celery import Celery, Task
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
DATABASE_URL = os.environ.get('DATABASE_URL')


class CeleryConfig:
    # CELERY_IMPORTS = ('proj.tasks')
    CELERY_RESULT_EXTENDED = True
    CELERY_TASK_RESULT_EXPIRES = 30
    # CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json'
    # CELERY_TASK_SERIALIZER = 'json'
    # CELERY_RESULT_SERIALIZER = 'json'
    # CELERY_TIMEZONE = 'Asia/Seoul'
    CELERY_ENABLE_UTC = False
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/0')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    REDIS_HOST = 'localhost'
    REDIS_PASSWORD = ''
    REDIS_PORT = 6379
    REDIS_URL = 'redis://localhost:6379/0'


CLCFG = dict(
    broker_url=BROKER_URL,
    result_backend=RESULT_BACKEND,
    task_ignore_result=True,
    accept_content=['application/json'],
    broker_connection_retry_on_startup=True,
    beat_schedule={
        "get_customer": {
            "task": "get_customer_type",
            "schedule": crontab("*"),
            'args': (1,)
        }
    },
)


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.import_name,
                        broker=BROKER_URL,
                        backend=RESULT_BACKEND,
                        result_extended=True, task_cls=FlaskTask)

    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def create_app():
    from flask import Flask
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    api = Api(app)
    app.config.from_object(DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config.from_mapping(CELERY=CLCFG)
    with app.app_context():
        db.init_app(app)
    # migrate = Migrate()
    # migrate.init_app(app, db)
    Migrate(app, db)

    celery_init_app(app)

    admin = Admin(app, name='mss', template_mode='bootstrap3')

    app.register_blueprint(wrk, url_prefix='/task/')
    api.add_resource(ApiAllType, '/api/types/')  # API
    api.add_resource(ApiAllTypeParam, '/api/type/<int:id>')  # API
    api.add_resource(ApiFifo, '/fifo/publisher/')  # API
    api.add_resource(ApiFifoConsumer, '/fifo/consumer/')  # API

    admin.add_view(ModelView(AllTypes, db.session))

    return app

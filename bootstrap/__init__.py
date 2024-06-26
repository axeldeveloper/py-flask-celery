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
from flask_seeder import FlaskSeeder

BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
DATABASE_URL = os.environ.get('DATABASE_URL')

# CONFIGURAÇÃO DE TAREFA PERIODICA NO CLERY
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



# CREATE APP FLASK
def create_app():
    from flask import Flask
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    api = Api(app)
    app.config.from_object(DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config.from_mapping(CELERY=CLCFG)
    with app.app_context():
        db.init_app(app)

    # MIGRATE
    # migrate.init_app(app, db)
    Migrate(app, db)

    #SEED
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    # CELERY
    celery_init_app(app)

    admin = Admin(app, name='mss', template_mode='bootstrap3')

    app.register_blueprint(wrk, url_prefix='/task/')
    api.add_resource(ApiAllType, '/api/types/')  # API
    api.add_resource(ApiAllTypeParam, '/api/type/<int:id>')  # API
    api.add_resource(ApiFifo, '/fifo/publisher/')  # API
    api.add_resource(ApiFifoConsumer, '/fifo/consumer/')  # API

    admin.add_view(ModelView(AllTypes, db.session))

    return app

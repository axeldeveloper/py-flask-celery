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

def init_celery(app):
    # For reference
    # https://flask.palletsprojects.com/en/2.2.x/patterns/celery/
    from celery import Celery

    # celery = Celery(app.import_name)
    celery = Celery(app.import_name, broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    celery_app = init_celery(app)
    with app.app_context():
        db.init_app(app)
    # db.init_app(app)
    migrate.init_app(app, db)
    #migrate = Migrate(app, db)
    app.register_blueprint(wrk, url_prefix='/task/')
    return app, celery_app

def create_celery_app(app=None):
    app = app or create_app()
    #celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery = Celery(__name__, broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
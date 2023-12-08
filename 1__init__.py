import os

# Celery settings
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
DATABASE_URL = os.environ.get('DATABASE_URL')

def init_celery(app):
    # For reference
    # https://flask.palletsprojects.com/en/2.2.x/patterns/celery/
    from celery import Celery

    # celery = Celery(app.import_name)
    celery = Celery(app.import_name, broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
    celery.conf.update(app.config['CELERY_CONFIG'])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


# def create_app():
# 	# Imports here keep things out of the global scope
# 	# Its only available in the local scope
# 	from flask import Flask
#
# 	flask_app = Flask(__name__)
# 	flask_app.config.from_object('config.settings')
# 	celery_app = init_celery(flask_app)
#
# 	return (flask_app, celery_app)


# run.py
# from project import create_app

#Yeah, but does all of this even work?
#flask_app, celery_app = create_app()


# running flask example
#flask --app run:flask_app run --host=0.0.0.0

# running celery worker example
#celery --app run.celery_app worker --loglevel=info
from datetime import datetime, timedelta
import time
from redis import Redis
from setting import Config
import tasks
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
import os

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_TASK_TRACK_STARTED = True




#app = Celery(__name__)
#app.config_from_object(Config)
task_ignore_result=False
app = Celery('tasks',
            broker=CELERY_BROKER_URL,
            backend=CELERY_RESULT_BACKEND, result_extended=True)

#app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", CELERY_BROKER_URL)
#app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", CELERY_RESULT_BACKEND)
logger = get_task_logger(__name__)


@app.task(name="task_add")
def add(x, y):
    #logger.info('Adding {0} + {1}'.format(x, y))
    return x + y

@app.task(name="task_backend")
def task_backend() -> str:
    #logger.info('REDIS {0} '.format(CELERY_RESULT_BACKEND))
    return 'Request: {0!r}'.format(CELERY_RESULT_BACKEND)

@app.task(name="task_print")
def task_print(seconds):
    print("Starting task")
    for num in range(seconds):
        print(num, ". Hello World!")
        time.sleep(1)
    print("Task completed")
    return True

def t_status(id):
    c = app.AsyncResult(id)
    return c



def print_numbers(seconds):
    print("Starting num task")
    for num in range(seconds):
        print(num)
        time.sleep(1)
    print("Task to print_numbers completed")
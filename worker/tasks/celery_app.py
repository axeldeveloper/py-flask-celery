import os
from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
# Celery settings
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
# CELERY_TASK_TRACK_STARTED = True

task_ignore_result = False
app = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
logger = get_task_logger(__name__)


@app.task(name="sum_value", default_retry_delay=30, max_retries=5)
def sum_value(x, y):
    # logger.info('Adding {0} + {1}'.format(x, y))
    return x + y
#
@app.task(name="task_backend")
def task_backend() -> str:
     #logger.info('REDIS {0} '.format(CELERY_RESULT_BACKEND))
     return 'Request: {0!r}'.format(RESULT_BACKEND)

app.conf.beat_schedule = {
    "birthday-task": {
        "task": "tasks.task_backend",
        "schedule": crontab(hour=7, minute=0)
    }
}


# @app.task(name="task_print")
# def task_print(seconds):
#     print("Starting task")
#     for num in range(seconds):
#         print(num, ". Hello World!")
#         time.sleep(1)
#     print("Task completed")
#     return True
#
# def t_status(id):
#     c = app.AsyncResult(id)
#     return c
#
#
#
# def print_numbers(seconds):
#     print("Starting num task")
#     for num in range(seconds):
#         print(num)
#         time.sleep(1)
#     print("Task to print_numbers completed")

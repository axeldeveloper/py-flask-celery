import os
import time
from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from celery.signals import task_revoked
from services.service_all_types import ServiceAllTypes

# Celery settings
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')

task_ignore_result = False
celery = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
logger = get_task_logger(__name__)

# app.control.add_consumer(
#     queue='trabalho',
#     exchange='trabalho',
#     reply=True, destination=['w1@example.com', 'w2@example.com'])

celery.conf.beat_schedule = {}

celery.conf.CELERYBEAT_SCHEDULE = {
    # 'call-every-30-seconds': {
    #     'task': 'task_backend',
    #     'schedule': 30.0,
    #     'args': ("call-every-30-seconds",)
    # },
    # "call-birthday-task": {
    #     "task": "task_backend",
    #     "schedule": crontab(minute="*"),
    #     'args': ("call-birthday-task",)
    # },
    # Executes every minute
    'periodic_task-every-minute': {
        'task': 'task_print',
        'schedule': crontab(minute="*"),
        'args': (1,)
    },
}

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # sender.add_periodic_task(10.0, test.s('hello every 10 seconds.'), name='Every 10')

    # sender.add_periodic_task(30.0, test.s('every every 30 seconds.'), name='Every 30')

    # sender.add_periodic_task(30.0, test.s('expires every 10 seconds'), expires=2)

    sender.add_periodic_task(
        # crontab(hour=7, minute=30, day_of_week=1),  # Executes every Monday morning at 7:30 a.m.
        crontab(minute="*"),
        test.s('cada minuto!'),
    )

@task_revoked.connect
def on_task_revoked(*args, **kwargs):
    print(str(kwargs))
    print('======================================= task_revoked ===================================================')


@celery.task
def test(arg):
    print(arg)


# @app.task(name="sum_value", default_retry_delay=10, max_retries=2)
@celery.task(name="sum_value", default_retry_delay=2 * 60, max_retries=2, rate_limit=5)
def sum_value(x, y):
    return x + y


#
@celery.task(name="task_backend")
def task_backend(x) -> str:
    return f'Request: {x}'



@celery.task(name="task_print")
def task_print(u_id):
    print("Starting task")
    with app.app_context():
        # DB interactions
        row = ServiceAllTypes().findOne(u_id)
        # for num in range(seconds):
        #     print(num, ". Hello World!")
    time.sleep(1)
    print("Task completed")
    return row
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

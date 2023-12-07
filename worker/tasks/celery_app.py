import os
from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from celery.signals import task_revoked

# Celery settings
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
# CELERY_TASK_TRACK_STARTED = True

task_ignore_result = False
app = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
logger = get_task_logger(__name__)

# app.control.add_consumer(
#     queue='trabalho',
#     exchange='trabalho',
#     reply=True, destination=['w1@example.com', 'w2@example.com'])

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello every 10 seconds.'), name='add every 10')

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    sender.add_periodic_task(30.0, test.s('every every 30 seconds.'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('expires every 10 seconds'), expires=2)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        #crontab(hour=7, minute=30, day_of_week=1),
        crontab(minute=1),
        test.s('Happy Mondays!'),
    )

@task_revoked.connect
def on_task_revoked(*args, **kwargs):
    print(str(kwargs))
    print('======================================= task_revoked ===================================================')

@app.task
def test(arg):
    print(arg)

# @app.task(name="sum_value", default_retry_delay=10, max_retries=2)
@app.task(name="sum_value",  max_retries=2)
def sum_value(x, y):
    return x + y
#
@app.task(name="task_backend")
def task_backend() -> str:
     return 'Request: {0!r}'.format(RESULT_BACKEND)

app.conf.beat_schedule = {
    "birthday-task": {
        "task": "tasks.task_backend",
        # "schedule": crontab(hour=7, minute=0)
        # "schedule": crontab(minute=1)
        "schedule": crontab(minute="*")
        #'schedule': 30.0,
        #'args': (16, 16)


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

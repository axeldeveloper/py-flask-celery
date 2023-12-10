import os

from app import create_app
from worker.tasks.celery_worker import TextTransformer

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
celery_app.conf.update(
    CELERY_BROKER_URL=os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/0'),
    CELERY_RESULT_BACKEND=os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0'),
    CELERY_TASK_SERIALIZER='json',
    CELERY_IGNORE_RESULT=False,
)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
#     # crontab(hour=7, minute=30, day_of_week=1),  # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(10.0, run_message.s('hello every 10 seconds.'), name='Every 10')
      sender.add_periodic_task(30.0, TextTransformer().run_msg.s('every every 30 seconds.'), name='Every 30')
#     # sender.add_periodic_task(30.0, run_message.s('expires every 10 seconds'), expires=2)
#     sender.add_periodic_task(crontab(minute="*"), run_message.s('cada minuto!'), )


# celery_app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'run_msg',
#         # 'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'schedule': 10,
#         'args': ("TESTE" , ),
#     },
# }
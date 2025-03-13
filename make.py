import os

from app import create_app
from worker.tasks.celery_worker import TextTransformer
from celery.schedules import crontab

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
celery_app.conf.update(
    # ATUALIZAR AS CONFIGURAÇOES 
    CELERY_IGNORE_RESULT=False,
)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    crontab(hour=7, minute=30, day_of_week=1),  # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(30.0, TextTransformer().run_msg.s('every every 30 seconds.'), name='Every 30', expires=2)
    #sender.add_periodic_task(crontab(minute="*"), run_message.s('cada minuto!'), )
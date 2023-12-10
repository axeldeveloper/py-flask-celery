# """
# Run using the command:
#
# python celery -A worker.tasks.celery_app worker --loglevel=INFO --concurrency=2 -E -l info
# """
#
# import json
# import os
# import time
# from celery import Celery, Task
# from celery.utils.log import get_task_logger
# from celery.schedules import crontab
# from celery.signals import task_revoked
# from sqlalchemy.exc import NoResultFound
# from models.all_type import AllTypes
# from models.orm_session import db_session
#
#
# # Celery settings
# BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
# RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
# DATABASE_URL = os.environ.get('DATABASE_URL')
#
# task_ignore_result = False
# celery = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND, result_extended=True)
# logger = get_task_logger(__name__)
# dbsession = None
#
# celery.conf.beat_schedule = {}
#
# # CELERYBEAT_SCHEDULE
# # celery.conf.CELERYBEAT_SCHEDULE = {
# #     # Executes every minute
# #     'periodic_task-every-minute': {
# #         'task': 'check_customer',
# #         'schedule': crontab(minute="*"),
# #         'args': (1,)
# #     },
# # }
#
#
# class SqlAlchemyTask(Task):
#     abstract = True
#     _db = None
#     _mandrill = None
#
#     # @property
#     # def db(self):
#     #     if self._db is not None:
#     #         return self._db
#     #     self._db = psycopg2.connect(
#     #         host=self.app.conf.POSTGRES_HOST,
#     #         port=self.app.conf.POSTGRES_PORT,
#     #         dbname=self.app.conf.POSTGRES_DBNAME,
#     #         user=self.app.conf.POSTGRES_USER,
#     #         password=self.app.conf.POSTGRES_PASSWORD,
#     #         cursor_factory=NamedTupleCursor,
#     #         connection_factory=Connection,
#     #     )
#     #     return self._db
#
#     def after_return(self, status, retval, task_id, args, kwargs, einfo):
#         """
#         Clean up database after the task is finished.
#
#         """
#         # db_session.remove()
#         # self._db.close()
#         self._db = None
#
#
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     initialize_session()
#     # crontab(hour=7, minute=30, day_of_week=1),  # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(10.0, run_message.s('hello every 10 seconds.'), name='Every 10')
#     # sender.add_periodic_task(30.0, run_message.s('every every 30 seconds.'), name='Every 30')
#     # sender.add_periodic_task(30.0, run_message.s('expires every 10 seconds'), expires=2)
#     sender.add_periodic_task(crontab(minute="*"), run_message.s('cada minuto!'), )
#
#
# @task_revoked.connect
# def on_task_revoked(*args, **kwargs):
#     print(str(kwargs))
#     print('======================================= task_revoked ===================================================')
#
#
# @celery.task(name="run_message", )
# def run_message(arg):
#     print(arg)
#
#
# @celery.task(name="sum_value", default_retry_delay=2 * 60, max_retries=2, rate_limit=5)
# def sum_value(x, y):
#     return x + y
#
#
# @celery.task(name="task_backend")
# def task_backend(x) -> str:
#     return f'Request: {x}'
#
#
# @celery.task(base=SqlAlchemyTask, name="check_customer")
# def check_customer_type(u_id):
#     try:
#         logger.debug("Starting task")
#         # row = db_session.query(AllTypes).filter(AllTypes.id == u_id).one()
#         row = db_session.query(AllTypes).get(u_id)
#         time.sleep(1)
#         if row.type_name == "financeiro":
#             logger.info("Task completed")
#             return "ok 1"
#         else:
#             logger.info("Task completed")
#             return "Não"
#         # return json.dumps(row.name)
#         # return json.dumps(s.as_dict())
#     except (Exception, ValueError, NoResultFound) as exc:
#         raise check_customer_type.retry(exc=exc)
#
#

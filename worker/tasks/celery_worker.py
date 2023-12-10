#!/usr/bin/env python

"""
Run using the command:

python celery -A worker.tasks.celery_app worker --loglevel=INFO --concurrency=2 -E -l info
"""
import time
from celery import current_app, current_task
from celery.result import AsyncResult
from celery.utils.log import get_task_logger
from sqlalchemy.exc import NoResultFound
from services.service_all_types import ServiceAllTypes

logger = get_task_logger(__name__)
task_ignore_result = False


class TextTransformer:

    def __init__(self):
        self.a = 0

    @staticmethod
    @current_app.task(name="status")
    def status(task_id: str):
        res = AsyncResult(task_id)
        return res

    @staticmethod
    @current_app.task(name="run_msg")
    def run_msg(arg):
        print(arg)

    @staticmethod
    @current_app.task(name="class_test")
    def add(total):
         for i in range(total):
             print(i)
         return {"current": 100, "total": total, "status": "Complete."}

    @staticmethod
    @current_app.task(name="uppercase", default_retry_delay=2 * 60, max_retries=2, rate_limit=5)
    def uppercase(test):
        try:
            return test.upper()
        except (Exception, ValueError, NoResultFound) as exc:
            raise TextTransformer().uppercase.retry(exc=exc)

    @current_app.task(name="get_customer_type")
    def get_customer_type(u_id: int):
        try:
            logger.debug("Starting task")
            # row = db_session.query(AllTypes).filter(AllTypes.id == u_id).one()
            # row = db_session.query(AllTypes).get(u_id)
            row = ServiceAllTypes().findOne(u_id)
            time.sleep(1)
            if row["type_name"] == "financeiro":
                logger.info("Task completed")
                return "ok"
            else:
                logger.info("Task completed")
                return "Não"
            # return row
            # return json.dumps(s.as_dict())
        except (Exception, ValueError, NoResultFound) as exc:
            raise TextTransformer().get_customer_type.retry(exc=exc)

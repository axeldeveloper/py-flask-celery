#!/usr/bin/env python
import time

from celery import current_app
from celery.utils.log import get_task_logger
from sqlalchemy.exc import NoResultFound
from services.service_all_types import ServiceAllTypes
from setting.config import DevelopmentConfig
from celery.schedules import crontab

logger = get_task_logger(__name__)
task_ignore_result = False

# current_app.conf.update(DevelopmentConfig)
#current_app.config['DISABLED '] = False
#current_app.conf['DISABLED'] = True
# current_app.conf.CELERYBEAT_SCHEDULE = {
#     'periodic_task-every-minute': {
#         'task': 'check_customer',
#         'schedule': crontab(minute="*"),
#         'args': (1,)
#     },
# }

# current_app.conf['CELERYBEAT_SCHEDULE'] = {
#     'periodic_task-every-minute': {
#         'task': 'check_customer',
#         'schedule': crontab(minute="*"),
#         'args': (1,)
#     },
# }

@current_app.task(name="substract_value", default_retry_delay=2 * 60, max_retries=2, rate_limit=5)
def substract_value(x, y):
    return x + y


@current_app.task(name="get_customer_type")
def get_customer_type(u_id):
    try:
        logger.debug("Starting task")
        # row = db_session.query(AllTypes).filter(AllTypes.id == u_id).one()
        # row = db_session.query(AllTypes).get(u_id)
        row = ServiceAllTypes().findOne(u_id)
        time.sleep(1)
        if row.type_name == "financeiro":
            logger.info("Task completed")
            return "ok 1"
        else:
            logger.info("Task completed")
            return "Não"
        # return json.dumps(row.name)
        # return json.dumps(s.as_dict())
    except (Exception, ValueError, NoResultFound) as exc:
        raise get_customer_type.retry(exc=exc)


from typing import Tuple

from flask import Blueprint, jsonify, Response, request
from worker.tasks import celery_worker
from worker.tasks.celery_worker import TextTransformer

wrk = Blueprint('api_worker', __name__)

# PENDING、STARTED、RETRY、FAILURE、SUCCESS
@wrk.route('/uppercase')
def uppercase():
    #result = celery_worker.substract_value.delay(5, 4)
    #result = celery_app.sum_value.apply_async(args=[5, 5], countdown=60)
    result = celery_worker.TextTransformer().uppercase.apply_async(args=["clery"], countdown=10)
    while not result.ready():
         pass
    print(result.get())
    return jsonify({"status": result.state, "message": result.get(), "result_id": result.id}), 200

@wrk.get("/status/<uuid>")
def task_result(uuid: str) -> tuple[Response, int]:
    task_result = celery_worker.t_status(uuid)
    print(task_result)
    # if res.state == "SUCCESS":
    #     return "success"
    # else:
    #     return "progress"
    result = {
        "task_id": id,
        "successful": task_result.status,
        "value": task_result.result,
    }
    return jsonify(result), 200

@wrk.route('/myrota', defaults={'q' : '25'})
def myrote(q):
    source = request.args['q']
    return '''<h1>The source value is: {}</h1>'''.format(source)

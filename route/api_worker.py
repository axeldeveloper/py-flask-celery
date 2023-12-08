from flask import Blueprint, render_template, abort, jsonify, request
from jinja2 import TemplateNotFound
from os import environ

from services.service_all_types import ServiceAllTypes
from setting.standar_error import StandarError
from worker.tasks import celery_app, celery_worker

wrk = Blueprint('api_worker', __name__)

@wrk.route('/sum')
def sum_value():
    # result = celery_app.sum_value.delay(5, 4)
    result = celery_app.sum_value.apply_async(args=[5,5], countdown=60)
    while not result.ready():
        pass
    print(result.get())
    return jsonify({
        "status": result.state,
        "message": result.get(),
        "result_id": result.id}), 200

@wrk.route('/substract')
def substract():
    result = celery_worker.substract_value.delay(5, 4)
    #result = celery_worker.substract_value.apply_async(args=[5,5], countdown=60)
    # while not result.ready():
    #     pass
    # print(result.get())
    return jsonify({
        "status": result.state,
        "message": result.get(),
        "result_id": result.id}), 200

# @app.route('/teste2')
# def teste2():
#     resto = tasks.task_backend.delay()
#     #print(resto.wait())
#     return jsonify({ "status": resto.state, "message": 'rest', "result_id": resto.id}), 200
#
# @app.route('/teste3')
# def teste3():
#     resto = tasks.task_print.delay(5)
#     #print(resto.wait())
#     return jsonify({ "status": resto.state, "message": 'rest', "result_id": resto.id}), 200
#
#
# @app.get("/status/<id>")
# def task_result(id: str) -> dict[str, object]:
#     #task_result  = AsyncResult(id)
#     task_result  = tasks.t_status(id)
#     #task_result = AsyncResult(id, app=app)
#     result = {
#         "task_id": id,
#         "successful": task_result.status,
#         "value": task_result.result,
#     }
#     return jsonify(result), 200
#

# @wrk.route('/simple/<page>')
# def show(page):
#     try:
#         abort(404)
#         return {'hello': 'world world', 'page': page}
#     except TemplateNotFound:
#         abort(404)
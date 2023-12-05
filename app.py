from flask import Flask, jsonify
# from simple_page import simple_page
# from celery.result import AsyncResult
# import tasks
# import redis
# import time

app = Flask(__name__)
# app.register_blueprint(simple_page)

# redis_connection = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/v1")
def v1():
    return "<h1 style='color:blue'>Hello There!</h1>"

# @app.route('/teste1')
# def count_visit():
#     rest = tasks.add.delay(5, 4)
#     return jsonify({"status": rest.state, "message": 'rest', "result_id": rest.id}), 200
#
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



#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5002, debug=False)
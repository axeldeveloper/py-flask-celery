import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from models.database import db
from route.api_all_type import ApiAllType, ApiAllTypeParam
from route.simple_page import simple
from setting.config import DevelopmentConfig
from worker.service_rabbitmq import ServiceRabbitmq
from flask_restful import Api
from jinja2 import TemplateNotFound
from flask_sqlalchemy import SQLAlchemy

# from celery.result import AsyncResult
# import tasks
# import redis
# import time
app = Flask(__name__)
# db = SQLAlchemy(app)
api = Api(app)
app.config.from_object(DevelopmentConfig)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(simple, url_prefix='/api')
api.add_resource(ApiAllType, '/api/types/')
api.add_resource(ApiAllTypeParam, '/api/type/<int:id>')

db.init_app(app)
migrate = Migrate(app, db)
# migrate = Migrate(app, db, command='migrate')
# redis_connection = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/")
def hello():
    return "<h1 style='color:blue'> Todo poderoso python !</h1>"

@app.route('/health')
def health():
    msg = os.environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg })


@app.route("/v1")
def v1():
    print(">>>>>" * 20)
    ServiceRabbitmq().publisher("Hello RabbitMQ!")
    print("ok")
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


# if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5002, debug=False)

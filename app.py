import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from models.database import db
from route.api_all_type import ApiAllType, ApiAllTypeParam
from route.api_worker import wrk
from setting.config import DevelopmentConfig
from worker import tasks
from worker.service_rabbitmq import ServiceRabbitmq
from flask_restful import Api
from worker.tasks import celery_app

app = Flask(__name__)
# db = SQLAlchemy(app)
api = Api(app)
app.config.from_object(DevelopmentConfig)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(wrk, url_prefix='/task/')
api.add_resource(ApiAllType, '/api/types/')
api.add_resource(ApiAllTypeParam, '/api/type/<int:id>')

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "<h1 style='color:blue'> Todo poderoso python !</h1>"

@app.route('/health')
def health():
    msg = os.environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg})


@app.route("/publisher")
def v1():
    print(">>>>>" * 20)
    ServiceRabbitmq().publisher("Hello RabbitMQ!")
    print("ok")
    return "<h1 style='color:blue'>Hello There!</h1>"

# if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5002, debug=False)

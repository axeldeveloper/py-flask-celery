import os

from flask import jsonify

from bootstrap import create_app
from worker.service_rabbitmq import ServiceRabbitmq

app, celery_app = create_app()


@app.route("/")
def home():
    return "<h1 style='color:blue'> Todo poderoso python !</h1>"

@app.route('/health')
def health():
    msg = os.environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg})


@app.route("/publisher")
def publisher():
    print(">>>>>" * 20)
    ServiceRabbitmq().publisher("Hello RabbitMQ!")
    print("ok")
    return "<h1 style='color:blue'>Hello There!</h1>"

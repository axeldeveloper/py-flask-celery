import os
from flask import jsonify, render_template, abort
from jinja2 import TemplateNotFound
from bootstrap import create_app


app = create_app()



# app, celery_app = create_app()
# celery_app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'run_msg',
#         # 'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'schedule': 30,
#         'args': ("TESTE" , ),
#     },
# }


@app.route("/")
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)



@app.route('/health')
def health():
    msg = os.environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg})


# @app.route("/publisher")


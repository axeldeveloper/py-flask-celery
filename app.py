import os
from flask import jsonify, render_template, abort
from jinja2 import TemplateNotFound
from bootstrap import create_app

app = create_app()

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


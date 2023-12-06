from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from os import environ

simple = Blueprint('simple_page', __name__)

@simple.route('/health')
def health():
    msg = environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg })

@simple.route('/simple/<page>')
def show(page):
    try:
        return {'hello': 'world world' , 'page': page}
    except TemplateNotFound:
        abort(404)


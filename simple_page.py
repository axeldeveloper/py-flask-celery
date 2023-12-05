from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from os import environ

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/health')
def health():
    msg = environ.get('FLASK_ENV')
    return jsonify({"status": "success", "message": msg })

@simple_page.route('/simple/<page>')
def show(page):
    try:
        return {'hello': 'world world' , 'page': page}
    except TemplateNotFound:
        abort(404)


from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/simple/<page>')
def show(page):
    try:
        return {'hello': 'world world' , 'page': page}
    except TemplateNotFound:
        abort(404)

@simple_page.route('/heel')
def hello_world():
    return jsonify({ "status": "success", "message": "Hello World!" })
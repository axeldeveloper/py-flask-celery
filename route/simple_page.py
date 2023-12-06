from flask import Blueprint, render_template, abort, jsonify, request
from jinja2 import TemplateNotFound
from os import environ

from services.service_all_types import ServiceAllTypes
from setting.standar_error import StandarError

simple = Blueprint('simple_page', __name__)

@simple.route('/all')
def get_all():
    """ Returns:  lists objects  """
    try:
        rows = ServiceAllTypes().findAll()

        return {'hello': 'world world', 'page': rows}
    except TemplateNotFound:
        abort(404)


@simple.route('/simple/<page>')
def show(page):
    try:
        abort(404)
        return {'hello': 'world world', 'page': page}
    except TemplateNotFound:
        abort(404)


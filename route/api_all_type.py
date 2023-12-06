from flask import request
from flask_restful import Resource

from services.service_all_types import ServiceAllTypes


class ApiAllType(Resource):

    def get(self):
        rows = ServiceAllTypes().findAll()
        return rows

    def post(self):
        data = request.get_json()
        response, data = ServiceAllTypes().create(data)
        if response:
            return data, 201  # 201 Created
        else:
            return {'message': "Unprocessable Entity"}, 422, {'Etag': 'Unprocessable Entity'}


class ApiAllTypeParam(Resource):

    def get(self, id):
        rows = ServiceAllTypes().findOne(id)
        return rows

    def put(self, id):
        data = request.get_json()
        response, data = ServiceAllTypes().update(data, id)
        if response:
            return data, 200  # 200 ok
        else:
            return {'message': "Unprocessable Entity"}, 422, {'Etag': 'Unprocessable Entity'}

    def delete(self, id):
        response, data = ServiceAllTypes().delete(id)
        if response:
            return data, 204   # 204 No Content
        else:
            return {'message': "Unprocessable Entity"}, 422, {'Etag': 'Unprocessable Entity'}

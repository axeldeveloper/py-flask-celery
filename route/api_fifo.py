
from flask_restful import Resource

from worker.service_rabbitmq import ServiceRabbitmq


class ApiFifo(Resource):

    
    def get(self):
        rows = ServiceRabbitmq().publisher("Hello RabbitMQ!")
        return rows
    

class ApiFifoConsumer(Resource):

    def get(self):
        rows = ServiceRabbitmq().consumer()
        return rows
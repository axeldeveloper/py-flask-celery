import pika

class Publisher:
    def __init__(self, exchange_name='my_exchange', routing_key='my_key'):
        self.exchange_name = exchange_name
        self.routing_key = routing_key

        credentials = pika.PlainCredentials('admin', 'demo123')


        # Conecta ao servidor RabbitMQ usando o protocolo AMQP
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
        self.channel = self.connection.channel()

        # Conecta ao servidor RabbitMQ usando o protocolo AMQP com nome de usuário e senha
        #credentials = pika.PlainCredentials("mss", "mss766312")
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-mss.alwaysdata.net', credentials=credentials))
        #self.channel = self.connection.channel()



        # Declara o exchange, se não existir
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')

    def publish_message(self, message):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message
        )
        print(f" [x] Sent '{message}'")

    def close_connection(self):
        self.connection.close()

# Exemplo de uso do Publisher
# publisher = Publisher()
# publisher.publish_message('Hello, RabbitMQ!')
# publisher.close_connection()

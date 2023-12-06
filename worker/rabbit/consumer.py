import pika

class Consumer:
    def __init__(self, exchange_name='my_exchange', queue_name='my_queue', routing_key='my_key'):
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.routing_key = routing_key

        # Conecta ao servidor RabbitMQ usando o protocolo AMQP
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        # Declara o exchange e a fila, se não existirem
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=self.routing_key)

        # Define o callback para processar as mensagens recebidas
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        print(f" [x] Received '{body}'")

    def start_consuming(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

# Exemplo de uso do Consumer
consumer = Consumer()
consumer.start_consuming()

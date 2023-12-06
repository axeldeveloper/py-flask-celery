from worker.rabbit.publisher import Publisher


class ServiceRabbitmq:

    def __int__(self, options=dict):
        self.options = options

    @staticmethod
    def publisher(mss: str):
        publisher = Publisher()
        publisher.publish_message(mss)
        publisher.close_connection()


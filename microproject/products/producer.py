import pika
import json

# RabbitMQ connection parameters
RABBITMQ_URL = 'amqps://wnpjboaw:u1nuV-x8XvZ3TwM6RwcfrmDhZo2lvoO_@fuji.lmq.cloudamqp.com/wnpjboaw'

def publish(method, body):
    try:
        # Create a new connection and channel for each publish
        params = pika.URLParameters(RABBITMQ_URL)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        # Publish message
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

        # Close connection after publishing
        connection.close()
    except Exception as e:
        print(f"Failed to publish message: {e}")

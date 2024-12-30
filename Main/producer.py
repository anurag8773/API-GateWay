import pika
import json

params = pika.URLParameters('YOUR_RABBITMQ_URL')

# Initialize connection and channel variables
connection = None
channel = None

def get_connection_and_channel():
    global connection, channel
    # Ensure connection is open, reconnect if necessary
    if not connection or connection.is_closed:
        connection = pika.BlockingConnection(params)
    # Ensure channel is open, recreate if necessary
    if not channel or channel.is_closed:
        channel = connection.channel()

def publish(method, body):
    # Ensure connection and channel are open before publishing
    get_connection_and_channel()
    properties = pika.BasicProperties(method)
    try:
        # Publish the message to the specified queue
        channel.basic_publish(
            exchange='', 
            routing_key='main', 
            body=json.dumps(body), 
            properties=properties
        )
    except Exception as e:
        print(f"Error publishing message: {e}")
        # You can implement retry logic here if necessary

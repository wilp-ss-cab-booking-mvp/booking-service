import pika
import json
from config import RABBITMQ_HOST, RABBITMQ_QUEUE
import logging

logging.basicConfig(level=logging.INFO)

def send_booking_notification(data):
    try:
        #Connects to RabbitMQ.
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE)

        #Publishes a message (as JSON string) to the target queue.
        message = json.dumps(data)
        logging.info(f"Publishing message to queue: {message}")
        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)
        print(f"[Booking Service] Sent message to queue: {message}")

        connection.close()
    except Exception as e:
        print(f"[Booking Service] Failed to send message: {str(e)}")
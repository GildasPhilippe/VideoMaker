import logging
import pika
import random as rd


PROCESSING_QUEUE_NAME = "video_processing"


def get_connection():
    credentials = pika.PlainCredentials('user', 'password')
    return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))


def add_session_id_to_queue(session_id):
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=PROCESSING_QUEUE_NAME, durable=True)
    logging.info(f"Adding to queue session_id {session_id}")
    channel.basic_publish(exchange='',
                          routing_key=PROCESSING_QUEUE_NAME,
                          body=session_id+str(rd.randint(0, 1000)))
    connection.close()
    logging.info(f"Added to queue session_id {session_id}")

from datetime import datetime, timezone
import logging
import os
import sys
import time

import pika
from pika.exceptions import AMQPConnectionError


PROCESSING_QUEUE_NAME = "video_processing"
MAX_TRY_CONNECTION = 10
TIME_BEFORE_RETRY = 3

logging.basicConfig(
    filename=f'./logs/logs-processor-{datetime.now(timezone.utc).strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    filemode='a'
)


def get_connection():
    credentials = pika.PlainCredentials('user', 'password')
    connection = None
    counter = 0
    while not connection and counter < MAX_TRY_CONNECTION:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
        except AMQPConnectionError:
            counter += 1
            logging.warning(f"Failed to connect for the {counter}th time ({counter}/{MAX_TRY_CONNECTION} tries)")
            if counter < MAX_TRY_CONNECTION:
                logging.info(f"Retrying in {TIME_BEFORE_RETRY} s")
            time.sleep(TIME_BEFORE_RETRY)
    return connection


def callback(ch, method, properties, body):
    logging.info(f""" Received {body.decode("utf-8")}""")
    time.sleep(5)
    logging.info("Ended processing")


def subscriber():
    logging.info('Setting up the subscription')
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=PROCESSING_QUEUE_NAME, durable=True)
    channel.basic_consume(queue=PROCESSING_QUEUE_NAME,
                          auto_ack=True,
                          on_message_callback=callback)
    logging.info('Waiting for messages')
    channel.start_consuming()


if __name__ == '__main__':
    subscriber()

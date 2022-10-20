import json
from typing import Dict

from pika import BlockingConnection, ConnectionParameters
from settings import mq_hostname, mq_vhost, mq_exchange_name


import send_mail
import console


def call(alerts):
    connection = BlockingConnection(
        ConnectionParameters(host='localhost', virtual_host='alerts_vHost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    result = channel.queue_declare(queue='test')
    channel.queue_bind(exchange='logs', queue=result.method.queue)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        alert: Dict = json.loads(body.decode('utf-8'))  # json.loads - from string to json
        alerts.insert(len(alerts), alert)
        console.init(alerts, alert)
        print(f" [x] Received message: {alert}")
        send_mail.call(alert["Site"], alert["Error"])

    channel.basic_consume(
        queue=result.method.queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
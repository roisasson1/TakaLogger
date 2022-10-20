import json
import pandas as pd

from pika import BlockingConnection, ConnectionParameters
from datetime import datetime


from settings import mq_hostname, mq_vhost, mq_exchange_name
from message import Message
import console


def call(name_of_site):
    connection = BlockingConnection(
        ConnectionParameters(host=mq_hostname, virtual_host=mq_vhost))
    channel = connection.channel()

    channel.exchange_declare(exchange=mq_exchange_name, exchange_type='fanout')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = Message(name_of_site, "טיים אאוט מעלית")


    message = {
        "Time": dt_string,
        "Site": msg.site,
        "Error": msg.error_type
    }

    console.init(name_of_site, message)

    channel.basic_publish(exchange=mq_exchange_name, routing_key='', body=json.dumps(message, indent=4, sort_keys=True, default=str))
    # json.dumps from json to string
    print(" [x] Sent %r" % message)
    connection.close()

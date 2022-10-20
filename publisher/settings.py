import os

mq_hostname = os.getenv("MQ_HOSTNAME") # get environment variable from os
mq_vhost = os.getenv("MQ_VHOST") # environment variables - in capital letters
mq_exchange_name = os.getenv("MQ_EXCHANGE_NAME")
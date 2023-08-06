import pika
import utils
import time

# <credentials> is used to authentication
credentials = pika.PlainCredentials('root', '000')


# block connection, connection is blocked until a specific response is returned
# sending paramete is available by <pika.ConnectionParameters>
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))


# <channel> is a wrapper for intracting with Rabbit-MQ
channel = connection.channel()


# queue needs name, if not sent, randomly initialized
channel.queue_declare(queue='q')



# for direct exchange use ''
# routing key is queue name
channel.basic_publish(exchange='', routing_key='q', body='hello', properties=pika.BasicProperties(
    # <properties> of message
    content_type='text/plain',
    content_encoding='gzip',
    # timestamp=1000000000,
    # expiration=str(time.time()),
    delivery_mode=2, # <delivery_mode>: 1: Write in RAM, 2: Write in DISK, effects on performance, by default is 1
    user_id='root',
    app_id='sender', # application name, can be consumer
    type='direct,q', # by your requirements, may be 'exchange_name,queue_name',
    headers={'sender':'root', 'receiver': 'others'},
    # other in documentation
))

print('sent')

connection.close()
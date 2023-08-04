import pika

# <credentials> is used to authentication
credentials = pika.PlainCredentials('root', '000')


# block connection, connection is blocked until a specific response is returned
# sending paramete is available by <pika.ConnectionParameters>
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))


# <channel> is a wrapper for intracting with Rabbit-MQ
channel = connection.channel()


# queue needs name, if not sent, randomly initialized
channel.queue_declare(queue='one')

# for direct exchange use ''
# routing key is queue name
channel.basic_publish(exchange='', routing_key='one', body='hello')

print('sent')

connection.close()
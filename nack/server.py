import pika
import time




credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='aj', exchange_type='fanout')
channel.queue_declare(queue='main')
channel.queue_bind('main', 'aj')

def callback(ch, method, properties, body):
    if method.delivery_tag % 5 == 0:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False, multiple=True)
        # for 1, 2, 3, 4 Divide remaining sent suddenly if remain should be 5
        #
    print(f'Receive: {method.delivery_tag}')


channel.basic_consume(queue='main', on_message_callback=callback)

print('Start Consuming ...')
channel.start_consuming()
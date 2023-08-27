import pika
import time




credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='main', exchange_type='direct', durable=True, auto_delete=False)
channel.queue_declare(queue='mainQ', durable=True, exclusive=False, auto_delete=False)
# in direct doesnt need  queue_bind
channel.queue_bind('mainQ', 'main')

def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(queue='mainQ', on_message_callback=callback)

print('Start Consuming ...')
channel.start_consuming()
import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='mainEX', exchange_type='direct')
channel.exchange_declare(exchange='dlEx', exchange_type='fanout')


channel.queue_declare(queue='mainQ', arguments={
    'x-dead-letter-exchange': 'dlEx',
    'x-message-ttl': 5000, # milisecond, # if time.sleep() is more than this time and the ack is after that, the messages NOT redirect to dlQ,
    # and is also in mainQ
    'x-max-length': 100
})
channel.queue_bind(exchange='mainEx', queue='mainQ', routing_key='home')


channel.queue_declare(queue='dlQ')
channel.queue_bind(queue='dlQ', exchange='dlEx')



def dlEx_callback(ch, method, properties, body):
    print(f'From dlEx: {body}')


def main_callback(ch, method, properties, body):
    time.sleep(10)
    print(f'From main : {body}')
    channel.basic_ack(delivery_tag=method.delivery_tag)



channel.basic_consume(queue='dlQ', on_message_callback=dlEx_callback, auto_ack=True)
channel.basic_consume(queue='mainQ', on_message_callback=main_callback)

print('Start Consuming ...')
channel.start_consuming()
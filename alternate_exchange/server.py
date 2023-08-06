import pika

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='altQ')
channel.queue_bind(exchange='altEx', queue='altQ')

channel.queue_declare(queue='mainQ')
# routing_key could be different from q name, 
# if routing_key not declared, it is automatically is the queue name 
channel.queue_bind(exchange='mainEx', queue='mainQ', routing_key='home')

def alt_callback(ch, method, properties, body):
    print(f'From Alt: {body}')


def main_callback(ch, method, properties, body):
    print(f'From main: {body}')


channel.basic_consume(queue='altQ', on_message_callback=alt_callback, auto_ack=True)
channel.basic_consume(queue='mainQ', on_message_callback=main_callback, auto_ack=True)

print('Start Consuming ...')
channel.start_consuming()
import pika



credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='destinationEx', exchange_type='fanout')

channel.queue_declare(queue='my_queue')

channel.queue_bind(exchange='destinationEx', queue='my_queue')
    

def callback(channel, mehtod, properties, body):
    print(f'Received: {body}')


channel.basic_consume(queue='my_queue', auto_ack=True, on_message_callback=callback)


print('server is running ...')

channel.start_consuming()
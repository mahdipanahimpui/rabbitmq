import pika


credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

# <durable> = False by default. write messages in DISK or just in RAM
channel.exchange_declare(exchange='topic_logs', exchange_type='topic', durable=False)

specific_queue = channel.queue_declare(queue='', exclusive=True)


# binding: is used to connect exchange to queue
# to set queue name, get it from rabbitmq(queue_declare)
channel.queue_bind(exchange='topic_logs', queue=specific_queue.method.queue, routing_key='*.*.not_important') # use #. insted *.*.

print('waiting for logs')
print('queue name: ', specific_queue.method.queue)

def callback(channel, method, properties, body):
    print(f'message: {body}')

channel.basic_consume(queue=specific_queue.method.queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()






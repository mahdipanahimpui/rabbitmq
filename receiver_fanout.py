import pika


credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

# <durable> = False by default. write messages in DISK or just in RAM
channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=False)

# every time that receriver_fanout.py is run, a new queue is declared, that is specific with oter queue(in terminal), so queue=''
# random naming is amq.random number
# how ever you can set queue name, 

# <exclusive>: the queue is exclusive for specific receiver that run it(queue),
# if connection of receiver to queue disconnected, the queue should be removed automatically
specific_queue = channel.queue_declare(queue='', exclusive=True)


# binding: is used to connect exchange to queue
# to set queue name, get it from rabbitmq(queue_declare)
channel.queue_bind(exchange='logs', queue=specific_queue.method.queue)

print('waiting for logs')
print('queue name: ', specific_queue.method.queue)

def callback(channel, method, properties, body):
    print(f'message: {body}')

channel.basic_consume(queue=specific_queue.method.queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()






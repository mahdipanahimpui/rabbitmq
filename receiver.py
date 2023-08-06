import pika


credentials = pika.PlainCredentials('root', '000')


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

# maybe receiver start first so declare is important,
# if queue exists, nothing
channel.queue_declare(queue='q')

# parameters is required
def callback(channel, method, properties, body):
    print(f'message: \n {body}')
    # properties that is sent
    # print(properties)
    # print(method)

    # sending ack end of computing
    channel.basic_ack(delivery_tag=method.delivery_tag)


# messages are sent one by one to the idle NODES, not a batch of them
channel.basic_qos(prefetch_count=1)

# auto_ack: if message is received, message remover from publisher queue
# by not using ack, message is not removed from the queue, so sending is topped and queue is more frequent
# using <auto_ack=True> in basic_consume is not normal, 
# it is prefered after computing the message(not just receiving) send an ack using method param
channel.basic_consume(queue='q', on_message_callback=callback)

print('Waiting for messages ...')

# keep app running for receiving messages
channel.start_consuming()


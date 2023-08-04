import pika


credentials = pika.PlainCredentials('root', '000')


connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

# maybe receiver start first so declare is important,
# if queue exists, nothing
channel.queue_declare(queue='one')

# parameters is required
def callback(channel, method, properties, body):
    print(f'message: \n {body}')

# auto_ack: if message is received, message remover from publisher queue
channel.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)

print('Waiting for messages ...')

# keep app running for receiving messages
channel.start_consuming()


import pika



credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='request_queue')

def on_request_message_received(channel, method, properties, body):
    print(f'received request: {properties.correlation_id}\n body: {body}')
    
    # reply request
    channel.basic_publish(exchange='', routing_key=properties.reply_to, body=f'reply to {properties.correlation_id}')

channel.basic_consume(queue='request_queue', auto_ack=True, on_message_callback=on_request_message_received)


print('server is running ...')

channel.start_consuming()
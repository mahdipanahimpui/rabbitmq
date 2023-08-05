import pika


credentials = pika.PlainCredentials('guest', 'guest')


connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

#insted using exchange_type='headers' use ExchangeType
channel.exchange_declare(exchange='headersEx', exchange_type='headers')
channel.queue_declare('headersEx-all-queue')



def callback(channel, method, properties, body):
    print(f'message: \n {body}')

bind_args = {
    'x-match':'all',
    'name':'mahdi',
    'age': '10'
}


channel.queue_bind(queue='headersEx-all-queue', exchange='headersEx', arguments=bind_args)
channel.basic_consume(queue='headersEx-all-queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages ...')

# keep app running for receiving messages
channel.start_consuming()


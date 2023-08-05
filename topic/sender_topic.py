import pika


### NOTE: in this senario:
## at first run the consumer then run sender, because queues is not declared in sender,
# declaring queue in sender is not required because of topic type

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

# to use other exchange, insted direct. declare an exchange
# <exchange> name, 
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')



messages = {
    'error.warning.important': 'this is an important message',
    'info.debug.not_important': 'this is an not important message'
}



for k,v in messages.items():
    channel.basic_publish(exchange='topic_logs', routing_key=k, body=v)


print('message sent.')

connection.close()












import pika

## nack ## <negative ack>

# negative ack:
#       basic_reject(delivery_tag=0, requeue=True)
#           delivery_tag: tag of message
#           requeue: put the message in queue again, use this if you have many consumer
#           note: if you have one consumer, loops of regect is happened
#           if dequeue is False, delete message or redirect in dead-leters, regect just one message




#       basic_nack(delivery_tag=0, requeue=True, multiple=False)
#       multiple: ack for multiple mesages



credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

# accept/regect
channel.exchange_declare(exchange='aj', exchange_type='fanout')

while True:
    channel.basic_publish(exchange='aj', routing_key='home', body='hello_world!')
    print('Sent...!')
    input('Press any key to continue ...!')
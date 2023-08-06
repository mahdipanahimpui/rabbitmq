import pika

## dead letters ##

# if message not received by consumer(message rejected or negative ack)
# meesage expire time
# queue length-limit

# you can sent the message again to the main exchange as a new chance


credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()



channel.exchange_declare(exchange='mainEx', exchange_type='direct')
channel.basic_publish(exchange='mainEx', routing_key='home', body='hello world ...') ### routing_key not exists so altEx send it to altQ queue

print('Sent! ...')

connection.close()
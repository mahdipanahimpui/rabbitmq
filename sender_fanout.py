import pika


credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

# to use other exchange, insted direct. declare an exchange
# <exchange> name, 
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# routing_key='' because exchange type is fanout
channel.basic_publish(exchange='logs', routing_key='', body='FANOUT>>>')


print('message sent.')

connection.close()












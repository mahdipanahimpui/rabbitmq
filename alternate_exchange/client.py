import pika

## alternate exchange ##
## an exchange for unroutable messages or with false routing_key
# messages with false routing_key used to create logs

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()



channel.exchange_declare(exchange='altEx', exchange_type='fanout')
# assign the altEx to mainEx
channel.exchange_declare(exchange='mainEx', exchange_type='direct', arguments={'alternate-exchange': 'altEx'})

# routing key could be different from queue name 
# if routing_key is as same as queue name, routing_key is not required in queue_bind
channel.basic_publish(exchange='mainEx', routing_key='notEXists', body='hello world ...') ### routing_key not exists so altEx send it to altQ queue

print('Sent! ...')

connection.close()
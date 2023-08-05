import pika
from pika.exchange_type import ExchangeType

### NOTE: in this senario:
## at first run the consumer then run sender, because queues is not declared in sender,
# declaring queue in sender is not required because of headers type

# in this senario CONSUMER mention that message should receive or not

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

#insted using exchange_type='headers' use ExchangeType
channel.exchange_declare(exchange='headersEx', exchange_type=ExchangeType.headers)

# in headers routing_key=''
channel.basic_publish(exchange='headersEx', routing_key='', body='headers>>>',
                      properties=pika.BasicProperties(
                          headers={'name':'mahdi', 'age':'10'}
                          ))


print('message sent.')

connection.close()












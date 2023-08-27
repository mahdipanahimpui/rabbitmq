import pika

## confirm ## 
# a confirm to publisher from broker(not consumer), about getting message
# if durable is True, messages is writing on disk, but if befor writing the server restart happens the writting failed.
# to prevent that use confirm

# at first active the confirm service
# can use transaction instead of confirm, but transaction doesnt have good performance
import time

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel = connection.channel()

# durable=True wirte defination of exchange on disk, 
# auto_delete=False, if the last consumer connection to this exchange, dont delete the exchange(to continue exceptions, and debuging)
channel.exchange_declare(exchange='main', exchange_type='direct', durable=True, auto_delete=False)
# exclusive=False, multiple consumer can access to the queue
channel.queue_declare(queue='mainQ', durable=True, exclusive=False, auto_delete=False)


channel.queue_bind('mainQ', 'main', 'home')

# to active the confirm service
channel.confirm_delivery()


for i in range(20):
    try:
        # delivery_mode = 2, indicating that the message should be persisted to disk
        channel.basic_publish(exchange='main', routing_key='home', body='hello',
                              properties=pika.BasicProperties(content_type='text/plain', delivery_mode=2),
                              mandatory=True # if True, message that is not writen in broker, backs to publisher (when queue removed suddenly)
                              # if mandatory is False the unraotable messages, discarted or goes to alternative exchanges
                              )
        print(f'message {i} confirmed')
    except Exception as e:
        print(f'Exception: {type(e).__name__}')
    
    time.sleep(2)
        
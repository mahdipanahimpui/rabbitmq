import pika
import uuid

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()

###### در عین ناباوری با اینکه در کلاینت صف تعریف نشده است، ولی در صورتی که کلاینت زود‌ تر از سرور اجرا شود، سرور پیام‌های قبلی را هم نشان می‌دهد، واقعا سوال است که چرا؟؟ #####


channel.exchange_declare(exchange='sourceEx', exchange_type='direct')
channel.exchange_declare(exchange='destinationEx', exchange_type='fanout')

channel.exchange_bind(destination='destinationEx', source='sourceEx')
 
# in dirct, routing_key is required 
channel.basic_publish(exchange='sourceEx', routing_key='', body='message from publisher.')

print('message Sent ...')

connection.close()


























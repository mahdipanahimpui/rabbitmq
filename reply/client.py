import pika
import uuid

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()



# START: to get reply of message
reply_queue = channel.queue_declare(queue='', exclusive=True)

def on_reply_message_reiceved(channel, method, properties, body):
    print(f'reply message received: {body}')

channel.basic_consume(queue=reply_queue.method.queue, on_message_callback=on_reply_message_reiceved, auto_ack=True)
# END: to get reply of message




# START: to send messgae to server

channel.queue_declare(queue='requese_queue')
# produce correlation_id by using uuid module
cor_id = str(uuid.uuid4())
print(f'Request_id: {cor_id}')
channel.basic_publish(exchange='', routing_key='request_queue',
                      properties=pika.BasicProperties(
                          reply_to=reply_queue.method.queue, # reply_quue name
                          correlation_id=cor_id, # id of request message
                      ), 
                      body='my specific message')



print('client sending message.')


# channel.start_consuming() is required in client too
channel.start_consuming()
# End: to send messgae to server
























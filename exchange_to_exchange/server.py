import pika



credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))

channel = connection.channel()


    

channel.basic_consume(queue='request_queue', auto_ack=True, on_message_callback=on_request_message_received)


print('server is running ...')

channel.start_consuming()
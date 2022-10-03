from multiprocessing import connection
import pika

params = pika.URLParameters('amqps://ioeiotdf:D3Gx5iEXsf0ZrFX29gnbxYu6GxzACtja@shark.rmq.cloudamqp.com/ioeiotdf')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main ')
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
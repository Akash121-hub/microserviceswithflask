from multiprocessing import connection
import pika

params = pika.URLParameters('amqps://ioeiotdf:D3Gx5iEXsf0ZrFX29gnbxYu6GxzACtja@shark.rmq.cloudamqp.com/ioeiotdf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='main',body='hello')


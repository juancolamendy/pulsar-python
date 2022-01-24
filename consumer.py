import pulsar
import sys

consumer = 'consumer1'
if len(sys.argv)>1:
    consumer = sys.argv[1]

print('consumername: ' + consumer)

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('topic-01', subscription_name=consumer)

while True:
    try:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        consumer.acknowledge(msg)
    except Exception as ex:
        print('exception:', ex)
        consumer.negative_acknowledge(msg)

client.close()

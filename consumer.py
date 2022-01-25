import pulsar 
import sys

consumer = 'consumer1'
if len(sys.argv)>1:
    consumer = sys.argv[1]

print('consumername: ' + consumer)

# get client connection
client = pulsar.Client('pulsar://localhost:6650')

# open a subscription
consumer = client.subscribe('persistent://public/default/partitioned-topic', 
        subscription_name=consumer,
        initial_position=pulsar.InitialPosition.Latest,
        message_listener=None,
        negative_ack_redelivery_delay_ms=60000,
        #consumer_type=pulsar.ConsumerType.Exclusive
        #consumer_type=pulsar.ConsumerType.Shared
        consumer_type=pulsar.ConsumerType.KeyShared
        )

# processing loop
while True:
    try:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        consumer.acknowledge(msg)
    except Exception as ex:
        print('exception:', ex)
        consumer.negative_acknowledge(msg)

# close client
client.close()

import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('topic01', producer_name='producer')

for i in range(5):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()

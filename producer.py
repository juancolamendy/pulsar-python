import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('topic-01', producer_name='producer01')

for i in range(5):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()

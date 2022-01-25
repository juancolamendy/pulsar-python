import pulsar

# keys
keys = ['project_id:project-1', 'project_id:project-2', 'project_id:project-3']

# get client connection
client = pulsar.Client('pulsar://localhost:6650')

# create a producer
producer = client.create_producer('persistent://public/default/partitioned-topic', 
        producer_name='producer01',
        block_if_queue_full=True,
        batching_enabled=True,
        batching_max_publish_delay_ms=10)

# processing loop
for i in range(5):
    key = keys[i%3]
    msg = (f'msg: msg-{i} key: {key}').encode('utf-8')
    producer.send(msg,
            properties=None,
            partition_key=key)

# close client
client.close()

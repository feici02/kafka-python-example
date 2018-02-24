import json

from kafka import KafkaProducer
from kafka.errors import KafkaError


def check_future(future):
    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        print('Error')
        sys.exit(1)

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')
check_future(future)

# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')

# produce json messages
producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'),
        bootstrap_servers=['localhost:9092'])

future = producer.send('json-topic', {'key': 'value'})
check_future(future)


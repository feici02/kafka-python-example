import json
from kafka import KafkaConsumer

consumer = KafkaConsumer('json-topic',
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        bootstrap_servers=['localhost:9092'])

for message in consumer:
    print ("%s:%d:%d: value=%s" % (message.topic, message.partition,
        message.offset, message.value))


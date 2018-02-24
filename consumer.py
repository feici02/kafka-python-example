import sys
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic',
        group_id='my-group',
        bootstrap_servers=['localhost:9092'])

for message in consumer:
    print ("%s:%d:%d: value=%s" % (message.topic, message.partition,
        message.offset, message.value))


# kafka-python example

## Intsall Kafka and kafka-python
```
$ brew install kafka
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install kafka-python
```

## Start Kafka
```
$ brew services start kafka
$ brew services start zookeeper
```

## Start the two consumers
Start the two consumers in two separate termials
```
$ python consumer.py
$ python consumer2.py
```

## Run the producer
Run the producer in the third terminal, and check the output on previous two consumer terminals.
```
$ python producer.py
```

## Stop Kafka
```
$ brew services stop kafka
$ brew services stop zookeeper
```

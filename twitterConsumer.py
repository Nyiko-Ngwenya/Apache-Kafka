from kafka import KafkaConsumer
from setup import topicName
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topicName,
                         group_id='group_1',
                         bootstrap_servers=['localhost:9092'])

if consumer.bootstrap_connected() == False:
    raise Exception('You arent connected to the kafka server')

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                        message.offset, message.key,
                                        message.value))

#If we  need more thn one consumer
# consumer1 = KafkaConsumer('my-topic',
#                           group_id='my-group',
#                           bootstrap_servers='my.server.com')
# consumer2 = KafkaConsumer('my-topic',
#                           group_id='my-group',
#                           bootstrap_servers='my.server.com')
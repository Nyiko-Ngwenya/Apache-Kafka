from kafka import KafkaClient

client = KafkaClient(bootstrap_servers=['localhost:9092'])
if client.bootstrap_connected == 'False':
    raise Exception('You arent connected to the kafka server')
topicName = 'TwitterKafka'
client.add_topic(topicName)

# print(f"Created Topic called {topicName}")

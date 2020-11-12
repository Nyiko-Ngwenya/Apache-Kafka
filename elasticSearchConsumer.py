from kafka import KafkaConsumer
from setup import topicName
from elasticsearch import Elasticsearch
from secrets import main_host,username,password,host
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topicName,
                         group_id='kafka_elastic_search_v1',
                         bootstrap_servers=['localhost:9092'],auto_offset_reset ='earliest')

if consumer.bootstrap_connected() == False:
    raise Exception('You arent connected to the kafka server')
def getIDfromJSON(message):
    message = message.decode()
    message = json.loads(message)
    _id = int(message['id_str'])
    return _id

es = Elasticsearch(hosts=[host])

# i = 100
for message in consumer:
    _id = getIDfromJSON(message.value)
    es.create(index="twitter",id=_id,body=message.value,doc_type="tweets")
    print(f'ID {_id} has been sent to elasticsearch')
    # 
    # print(json.loads(message.value.decode()).keys())
    # i+=1
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                     message.offset, message.key,
    #                                     message.value))


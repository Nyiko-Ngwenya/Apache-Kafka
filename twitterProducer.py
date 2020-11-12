import tweepy
import webbrowser
import time
from secrets import api_key,api_secret ,access_token_secret,access_token
from setup import topicName
# auth = tweepy.OAuthHandler(api_key, api_secret)
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# Import KafkaProducer from Kafka library
from kafka import KafkaProducer

# Define server with port
# bootstrap_servers = 'localhost:9092'

# Define topic name where the message will publish
# topicName = 'pythonTwitter'

# Initialize producer variable
settings = {
    "bootstrap_servers":'localhost:9092',
    # "compression_type":'snappy',
    "batch_size":32*1024,
    "linger_ms":20,
    "acks":'all',
    "retries":1000,
    "max_in_flight_requests_per_connection":5 
}
producer = KafkaProducer(**settings)

if producer.bootstrap_connected() == False:
    raise Exception('You arent connected to the kafka server')

import json
class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
            
    def on_status(self, status):
        key = 'Python'.encode()
        information = json.dumps(status._json).encode()
        producer.send(topicName, information,key=key)
        print('Tweet sent to Kafka')
        

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
print('Starting to stream')
myStream.filter(track=['python'], is_async=False,languages=['en'])

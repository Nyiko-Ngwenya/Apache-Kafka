Setting up the environment
First of all you want to have installed Kafka and Zookeeper on your machine

pip install -r requirements.txt

Start your Zookeeper server and Kafka Broker before executing code.
Should you be running this on Linux or MACOS change the .bat to .sh

Zookeeper
zookeeper-server-start.bat config\zookeeper-properties

Kafka broker
kafka-server-start.bat config\server.properties

Zookeeper is running default on localhost:2181 and Kafka on localhost:9092.

kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic pythonTwitter 

We are currently working to use the KafkaClient to craete the above topic but for now use the CLI version.

PLEASE CREATE A TWITTER API PROJECT AND OBTAIN THE FOLLOWING api_key,api_secret ,access_token_secret,access_token and save them in secrets.py . If you plan on pushing to GITHUB remember to gitignore the secrets.py file or better (I will be implementing the system environment vatiables) for better security .

Now we can run 

python twitterConsumer.py 

to get read to consume the live tweets to Kafka

Now to get the actual tweets in a seperate command line

python twitterProducer.py 

AND WATCH THE TWEETS GO TO YOUR KAFKA TOPIC .


FOR ELASTICSEARCH

https://elasticsearch-py.readthedocs.io/en/master/index.html?highlight=Elasticsearch(

    
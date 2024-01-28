import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime

kafka_server = ['kafka:9092']
topic = "events"

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=kafka_server,
    api_version=(0,11,5),
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mongo_client = MongoClient("mongodb://mongodb")
db = mongo_client["myEventsDB"]
collection = db["events"]


for message in consumer:
    print("Received message from Kafka")
    event_data = message.value
    print("Event Data:", event_data)

    # Insert the event into MongoDB
    event_data["timestamp"] = datetime.strptime(event_data["timestamp"], '%Y-%m-%d-%H:%M:%S')
    collection.insert_one(event_data)
    print("Inserted into MongoDB")
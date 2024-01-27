import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime

kafka_server = ["localhost"]
topic = "events"

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=kafka_server,
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["myEventsDB"]  # Replace "mydatabase" with your desired database name
collection = db["events"]

for message in consumer:
    event_data = message.value
    print(event_data)

    # Insert the event into MongoDB
    event_data["timestamp"] = datetime.strptime(event_data["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
    collection.insert_one(event_data)


# import json
# from kafka import KafkaConsumer

# kafka_server = ["192.168.1.22"]

# topic = "test_topic"

# consumer = KafkaConsumer(
#     bootstrap_servers=kafka_server,
#     value_deserializer=json.loads,
#     auto_offset_reset="latest",
# )

# consumer.subscribe(topic)

# while True:
#     data = next(consumer)
#     print(data)
#     print(data.value)
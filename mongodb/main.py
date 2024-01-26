# mongodb-consumer/consumer.py

# from confluent_kafka import Consumer, KafkaError
# import pymongo
# from datetime import datetime
# from event import Event

import json
from kafka import KafkaConsumer

kafka_server = ["192.168.1.22"]

topic = "test_topic"

consumer = KafkaConsumer(
    bootstrap_servers=kafka_server,
    value_deserializer=json.loads,
    auto_offset_reset="latest",
)

consumer.subscribe(topic)

while True:
    data = next(consumer)
    print(data)
    print(data.value)

# kafka_conf = {
#     'bootstrap.servers': 'kafka:9092',
#     'group.id': 'my_consumer_group',
#     'auto.offset.reset': 'earliest'
# }

# consumer = Consumer(kafka_conf)
# topic = 'events'

# mongo_client = pymongo.MongoClient("mongodb://mongodb:27017/")
# db = mongo_client["events"]
# collection = db["event_collection"]

# consumer.subscribe([topic])

# while True:
#     msg = consumer.poll(1.0)

#     if msg is None:
#         continue
#     if msg.error():
#         if msg.error().code() == KafkaError._PARTITION_EOF:
#             continue
#         else:
#             print(msg.error())
#             break

#     # Deserialize the message value
#     event_data = json.loads(msg.value())
#     event_data["timestamp"] = datetime.strptime(event_data["timestamp"], '%Y-%m-%d %H:%M:%S')

#     event = Event(**event_data)

#     # Save the event to MongoDB
#     collection.insert_one(event_data)

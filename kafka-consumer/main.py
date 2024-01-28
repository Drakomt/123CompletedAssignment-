import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime


print("-------------------------------------------------------In Main.py-------------------------------------------------------------------------------------")

kafka_server = ["localhost:9092"]
topic = "events"

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=kafka_server,
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["myEventsDB"]  # Replace "mydatabase" with your desired database name
collection = db["events"]


# client = MongoClient("mongodb://localhost:27017/")
# db = client.users  # Replace "mydatabase" with your desired database name
# events = db.register

collection.insert_one({
    "reporterId": "1",
    "timestamp": "now",
    "metricId": "2",
    "metricValue": "12",
    "message": "test message",
})   #Test

for message in consumer:
    try:
        event_data = message.value
        print("Received message:", event_data)

        # Insert the event into MongoDB
        event_data["timestamp"] = datetime.strptime(event_data["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
        collection.insert_one(event_data)
        print("Inserted into MongoDB")
    except Exception as e:
        print("Error processing message:", str(e))


# for message in consumer:
#     event_data = message.value
#     print(event_data)

#     # Insert the event into MongoDB
#     event_data["timestamp"] = datetime.strptime(event_data["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
#     collection.insert_one(event_data)
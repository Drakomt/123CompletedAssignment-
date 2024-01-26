# from confluent_kafka import Producer
# import time
# from event import Event
import json
from datetime import datetime
from time import sleep
from random import choice
from kafka import KafkaProducer

kafka_server = ["localhost"]

topic = "test_topic"

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

random_values = [1, 2, 3, 4, 5, 6, 7]

while True:
    random_value = choice(random_values)
    data = {
        "test_data": {
            "random_value": random_value
        },
        "timestamp": str(datetime.now()),
        "value_status": "High" if random_value > 5 else "Low"
    }
    
    print(data)
    producer.send(topic, data)
    producer.flush()
    sleep(3)


# kafka_conf = {
#     'bootstrap.servers': 'kafka:9092',
# }

# producer = Producer(kafka_conf)
# topic = 'events'

# event = RandomEventGenerator()

# while True:
#     # Generate a random event
#     event_data = event.generate_event()

#     # Produce the event to Kafka topic
#     producer.produce(topic, key=str(event_data["reporterId"]), value=json.dumps(event_data))
#     producer.flush()

#     # Sleep for one second
#     time.sleep(1)

import json
from datetime import datetime
from time import sleep
from kafka import KafkaProducer
from event import Event

kafka_server = ['kafka:9092']
topic = "events"

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    api_version=(0,11,5),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

while True:
    event_instance = Event()
    event_data = event_instance.generate_event()
    print(event_data)
    producer.send(topic, event_data)
    producer.flush()
    sleep(1)

# redis-client/redis_client.py

import redis
import json
import time
from datetime import datetime
from event import Event

redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)

# Retrieve the last stored timestamp from Redis
last_timestamp_key = "last_timestamp"
last_timestamp_str = redis_client.get(last_timestamp_key)

# Set the initial timestamp to a very old date if not found in Redis
last_timestamp = datetime.strptime(last_timestamp_str, '%Y-%m-%d %H:%M:%S') if last_timestamp_str else datetime(1970, 1, 1)

while True:
    # Assume you have retrieved data from MongoDB
    # For demonstration purposes, I'm using a sample data list
    # Replace this with the actual logic to fetch data from MongoDB
    sample_data = [
        {
            "reporterId": 1,
            "timestamp": "2024-01-01 12:00:00",
            "metricId": 123,
            "metricValue": 42,
            "message": "Sample event message",
        },
        # Add more sample data as needed
    ]

    for event_data in sample_data:
        event_timestamp = datetime.strptime(event_data["timestamp"], '%Y-%m-%d %H:%M:%S')

        # Check if the event is newer than the last timestamp
        if event_timestamp > last_timestamp:
            # Save reporterId and timestamp to Redis
            redis_key = f"{event_data['reporterId']}_{event_data['timestamp']}"
            redis_client.set(redis_key, json.dumps(event_data, default=str))

    # Update the last timestamp in Redis
    last_timestamp = max(last_timestamp, event_timestamp)
    redis_client.set(last_timestamp_key, last_timestamp.strftime('%Y-%m-%d %H:%M:%S'))

    # Sleep for 30 seconds before checking for new data again
    time.sleep(30)

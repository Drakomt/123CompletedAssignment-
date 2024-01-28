import json
import redis
from pymongo import MongoClient
from datetime import datetime
import time

# Connect to MongoDB
mongo_client = MongoClient("mongodb://mongodb")
mongo_db = mongo_client["myEventsDB"]  # Replace with your MongoDB database name
mongo_collection = mongo_db["events"]

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

def get_latest_timestamp():
    # Retrieve the latest timestamp from Redis
    latest_timestamp = redis_client.get('latest_timestamp')
    if latest_timestamp:
        return datetime.strptime(latest_timestamp, '%Y-%m-%d-%H:%M:%S')
    return None

def update_latest_timestamp(timestamp):
    # Update the latest timestamp in Redis
    redis_client.set('latest_timestamp', timestamp.strftime('%Y-%m-%d-%H:%M:%S'))

def process_new_objects():
    # Get the latest timestamp from Redis
    latest_timestamp = get_latest_timestamp()

    # Query MongoDB for new objects since the latest timestamp
    query = {"timestamp": {"$gt": latest_timestamp}} if latest_timestamp else {}
    new_objects = list(mongo_collection.find(query).sort("timestamp", -1))

    # Debug prints
    print(f"---------------------Latest Timestamp from Redis: {latest_timestamp}---------------------")
    print(f"---------------------Query Timestamp Range: {latest_timestamp} - {datetime.now()}---------------------")

    # Process and insert new objects into Redis
    for obj in new_objects:
        key = f"{obj['reporterId']}:{datetime.strftime(obj['timestamp'],'%Y-%m-%d-%H:%M:%S')}"
        obj_json = json.dumps(obj, default=str)
        redis_client.set(key, obj_json)
        print(f"Inserted new object into Redis: {obj}")

    # Update the latest timestamp in Redis
    if new_objects:
        latest_timestamp = new_objects[-1]['timestamp']
        update_latest_timestamp(latest_timestamp)




def main():
    while True:
        process_new_objects()
        time.sleep(30)

if __name__ == "__main__":
    main()
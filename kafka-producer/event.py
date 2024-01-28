from faker import Faker
from datetime import datetime

class Event:
    fake = Faker()
    reporter_counter = 0  # Counter for incrementing reporterId

    @classmethod
    def generate_event(cls):
        cls.reporter_counter += 1  # Increment reporterId counter
        return {
            "reporterId": cls.reporter_counter,
            "timestamp": datetime.strftime(datetime.now(), '%Y-%m-%d-%H:%M:%S'),
            "metricId": cls.fake.random_int(min=1, max=1000),
            "metricValue": cls.fake.random_int(min=1, max=100),
            "message": cls.fake.text(),
        }
# random_event_generator.py

from faker import Faker

class Event:
    fake = Faker()

    @classmethod
    def generate_event(cls):
        return {
            "reporterId": cls.fake.random_int(min=1, max=100),
            "timestamp": cls.fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "metricId": cls.fake.random_int(min=1, max=1000),
            "metricValue": cls.fake.random_int(min=1, max=100),
            "message": cls.fake.text(),
        }


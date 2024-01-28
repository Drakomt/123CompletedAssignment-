# event.py

class Event:
    def __init__(self, reporterId, timestamp, metricId, metricValue, message):
        self.reporterId = reporterId
        self.timestamp = timestamp
        self.metricId = metricId
        self.metricValue = metricValue
        self.message = message


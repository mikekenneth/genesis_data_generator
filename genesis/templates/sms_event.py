from faker import Faker
from random import choice
from .base import BaseTemplate

fake = Faker()


class SmsEvent(BaseTemplate):
    def __init__(self):
        self.statuses = ("SUCCESS", "FAILED", "RETRY")
        self._template = "SmsEvent"
        self.sender = fake.msisdn()
        self.receiver = fake.msisdn()
        self.message = fake.sentence()
        self.status = choice(self.statuses)

    def data(self):
        return {"sender": self.sender, "receiver": self.receiver, "message": self.message, "status": self.status}

    def __repr__(self):
        return f'SMS(sender="{self.sender}", receiver="{self.receiver}", message="{self.message}", status="{self.status}")'

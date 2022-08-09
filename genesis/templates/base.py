from uuid import uuid4


class BaseTemplate:
    def __init__(self):
        self._id = str(uuid4())

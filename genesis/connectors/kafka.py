from kafka import KafkaProducer


class KafkaConnector:
    def __init__(self, bootstrap_servers: list, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    def __enter__(self, bootstrap_servers: list, topic: str):
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        if self.producer.bootstrap_connected:
            print(f"Sucessfully connected to: {self.bootstrap_servers}")
        else:
            print(f"Failed connection failed to: {self.bootstrap_servers}")

    def send_data(self, key=None, value=""):
        if not key:
            self.producer.send(topic=self.topic, value=value)
        else:
            self.producer.send(topic=self.topic, key=key, value=value)

    def __exit__(self):
        self.producer.close()

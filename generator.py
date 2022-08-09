from genesis.utils.helpers import get_section_credentials
from genesis.connectors.kafka import KafkaConnector
from genesis.templates.sms_event import SmsEvent

ini_file = ".config.ini"

kafka_creds = get_section_credentials(ini=ini_file, section="KAFKA")

bootstrap_servers = kafka_creds["servers"]

event = SmsEvent()
print(event)

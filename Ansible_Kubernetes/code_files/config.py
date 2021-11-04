#configuration details for kafka project

import os

kafka_server1 = os.getenv("KAFKA1")
# kafka_server2 = os.getenv("KAFKA2")

kafka_servers = [kafka_server1]
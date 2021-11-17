#!/usr/bin/python3
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
from kafka import KafkaConsumer  # consumer of events
import sys
import json
import couchdb
import os
import requests

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
kafka_servers = [os.getenv("KAFKA0"), os.getenv("KAFKA1")]
consumer = KafkaConsumer (bootstrap_servers=kafka_servers,
                          value_deserializer=lambda m: json.loads(m.decode('UTF-8')) )
print(consumer.topics())

# subscribe to topic
consumer.subscribe(topics=["ny"])



# settings for couchdb
couchdb_username = os.getenv("COUCHDB_USER")
couchdb_password = os.getenv("COUCHDB_PASSWORD")
couchdb_database = os.getenv("COUCHDB_DATABASE")
couchdb_host = os.getenv("COUCHDB_HOST")


# Connect to CouchDB
couch_db = couchdb.Server(f"http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/")
dbs = requests.get(f'http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/_all_dbs')

# Create Database - or access if already created

try:
    db = couch_db.create(couchdb_database)  # newly created
except Exception:
    db = couch_db[couchdb_database]  # existing
print("starting msg loop")
for msg in consumer:
    url = f'http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/{couchdb_database}/_bulk_docs'
    # Desteralize data and print message
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    docs = json.dumps({'docs': msg.value})
    # Save JSON document to CouchDB
    res2 = requests.post(url, headers=headers, data=docs)
    print('Received data', res2.content)

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close()
    







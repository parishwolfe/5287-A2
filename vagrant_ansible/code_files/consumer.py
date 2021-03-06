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
import config
import couchdb

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (bootstrap_servers=config.kafka_servers, api_version=(2,13,0))

# subscribe to topic
consumer.subscribe(topics=["ny", "chi"])

# Variables for CouchDB

# settings for couchdb
couchdb_username = 'admin'
couchdb_password = 'welcome'
couchdb_database = 'cloud_class'

# Connect to CouchDB
couch_db = couchdb.Server(f"http://{couchdb_username}:{couchdb_password}@129.114.27.189:5984/")

# Create Database - or access if already created

try:
    db = couch_db.create(couchdb_database)  # newly created
except:
    db = couch_db[couchdb_database]  # existing

for msg in consumer:
    # Desteralize data and print message
    msg = json.loads(str(msg.value, "ascii"))
    # Save JSON document to CouchDB
    print(msg)
    db.save(msg)

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close()
    







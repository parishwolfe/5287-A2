#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

# IMPORTS
import os  # need this for popen
import datetime
import time  # for sleep
import json
import sys
import pandas as pd

kafka_servers = [os.getenv("KAFKA1"), os.getenv("KAFKA2")]
from kafka import KafkaProducer  # producer of events


"""kafka-python docs: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html"""
import requests
import csv
from kafka.errors import KafkaTimeoutError


# GLOBAL FUNCTIONS
def get_api_key():
    """
    Get the API key from the environment variable
    """
    return os.environ.get("WEATHER_API_KEY")


def weather_request(city: str, api_key: str):
    """
    Make a request to the weather API and return the response
    LIMIT 60 calls per minute
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
        # return response.content
    else:
        return None

def main():
    # acquire the producer
    # api_version=(2,13,0)
    producer = KafkaProducer(bootstrap_servers=kafka_servers, acks=1)

    # wait for leader to write to log
    producer_id = sys.argv[1]
    topic = "ny"

    if producer_id == '1':
        filename = 'energy_pt1.csv'
    else:
        filename = 'energy_pt2.csv'

    index = 1
    header_list = ['id', 'timestamp', 'value', 'property', 'plug_id', 'household_id', 'house_id']
    for chunk in pd.read_csv(filename, names=header_list, skiprows=0, chunksize=1000):
        print('Batch sent:', index)
        print(chunk.to_json(orient="records"))
        producer.send(topic=topic, value=bytes(chunk.to_json(orient="records"),'UTF-8'))
        producer.flush()
        index += 1
        time.sleep(1)

    producer.close()

if __name__ == "__main__":
    main()

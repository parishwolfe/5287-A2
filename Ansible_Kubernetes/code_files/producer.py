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

def split_data(data, n):
    """Yield successive n-sized chunks from lst."""
    return [data[i:i + n] for i in range(0, len(data), n)]

def main():
    # acquire the producer
    # api_version=(2,13,0)
    producer = KafkaProducer(bootstrap_servers=kafka_servers, acks=1)

    # wait for leader to write to log
    producer_id = sys.argv[1]
    topic = "ny"

    batch_size = 1000

    if producer_id == '1':
        filename = 'energy_pt1.csv'
    else:
        filename = 'energy_pt2.csv'


    with open(filename, 'r') as csvfile:
            data = list(csv.reader(csvfile, delimiter=','))
            csvfile_split_up = split_data(data, batch_size)
            for i, data_chunk in enumerate(csvfile_split_up):
                message = {
                    'data': data_chunk,
                    'ts': datetime.datetime.now().isoformat(),
                    'producer_id': producer_id,
                    'message_number': i
                }
                message = bytes(json.dumps(message), 'ascii')

                producer.send(topic=topic, value=message)
                producer.flush()  # try to empty sending buffer
                print(message)

                time.sleep(5)

        # output = weather_request(city, api_key)


        # if output != None:
        #     # send the output to the Kafka topic
        #     message = {'City': output['name'],
        #                'Description': output['weather'][0]['description'],
        #                'Temperature': output['main']['temp'],
        #                'ts': datetime.datetime.now().isoformat()}
        #     print(message)
        #     # steralize data
        #     message = bytes(json.dumps(message), 'ascii')
        #     producer.send(topic=topic_, value=message)
        #     print("sent")
        #     producer.flush()  # try to empty the sending buffer
        #     print("flush")
        #     # sleep a second
        #     time.sleep(5)  # changed to 5 seconds for api limit
        # else:
        #     raise Exception("Error in send")

    # we are done
    producer.close()


if __name__ == "__main__":
    main()

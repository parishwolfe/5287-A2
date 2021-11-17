# Assignment 4 - CS5287

## Milestone 1 

### Checklist 
* Keep your entire setup from Assignment 3 as is. Split the huge data file (provided in the Assignment 4 directory) into two or three parts so that each producer can read appropriate amount of the data.
  * Done.  
* Modify your producer code so it can read their portion of the data, and takes, say 1000 records at a time, and sends them to one of the bootstrapped Kafka brokers. 
  * Done. Find code [here](https://github.com/parishwolfe/5287-A2/blob/main/Ansible_Kubernetes/code_files/producer.py)
* Kafka should then stream it to your consumer(this logic is same as before)
  * Done. Find code [here](https://github.com/parishwolfe/5287-A2/blob/main/Ansible_Kubernetes/code_files/consumer.py)
* Modify the consumer such that it can now take these incoming records and dump them into CouchDBso that CouchDB now has a complete batch of the data ready and available for Spark to use. 
  * Done. 



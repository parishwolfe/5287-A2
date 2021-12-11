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

### To run 

Look at instructions for Assignment 3 at https://github.com/parishwolfe/5287-A2/blob/main/README-A3.md. The code will be run the same way. The producers are now taking data from a csv file instead of using an API request. 

### Distrubition of work 

Both team memebers contributed equally. We met over zoom continously to stay in sync. 

### Demo 

A demo for this milestone can be found here: https://youtu.be/ChRZrBEsFC8

## Milestone 2

### Checklist

Map reduce code is [here](https://github.com/parishwolfe/5287-A2/blob/main/ScaffoldingCode/Spark_K8s_StandaloneCluster/mapReduce.py)

- Deploy Spark (you can deploy this manually; no Ansible; Docker and YAML files will be supplied)
  - done
- Develop appropriate code using Spark programming API to solve the MapReduce problem
  - done
- Develop some client code which will take the input data from CouchDB and sends it to Spark and then Spark dumps the results back into CouchDB as a different database.
  - done

### To Run

- Deploy spark cluster to kubernetes
- run the following command after kubectl exec to driver pod
```bash
 ${SPARK_HOME}/bin/spark-submit --master spark://spark-master-svc:7077 \
--properties-file ${SPARK_HOME}/conf/spark-driver.conf \
/mapReduce.py
```

### Distrobution of work

Both team memebers contributed equally. We met over zoom continously to stay in sync. 

### demo

![screenshot](https://github.com/parishwolfe/5287-A2/blob/main/ScaffoldingCode/Spark_K8s_StandaloneCluster/speed.png)

Video demonstration can be found here: 
https://www.youtube.com/watch?v=Exd7ETlHY6Y

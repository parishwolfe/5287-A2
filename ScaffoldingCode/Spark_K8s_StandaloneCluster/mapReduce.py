from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import couchdb
import requests
import os
import time
import pandas as pd

def get_documents_cdb():
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    return df

def mapReduce(dataframe):
    time_results = []
    for test in MR:
        print('10 iterations of MapReduce with M =', test[0], 'and R =', test[1])
        i = 1
        while i <= iterations:
            spark = SparkSession \
                .builder \
                .appName("AverageTest")\
                .config('spark.default.parallelism', test[0])\
                .config('spark.sql.shuffle.partitions', test[1])\
                .getOrCreate()
            df = spark.createDataFrame(dataframe)
            start = time.perf_counter()
            # map reduce result
            reduced = df.groupby(['house_id', 'household_id', 'plug_id']).agg(
                f.avg(f.when(df.property == 0, df.value)).alias('work'),
                f.avg(f.when(df.property == 1, df.value)).alias('load')).collect()
            end = time.perf_counter()
            time_diff = end - start
            time_results.append([test[0], test[1], i, time_diff])
            i += 1
            spark.stop()

    print("Finished MapReduce for all iterations")
    print("[MapWorkers, ReduceWorkers, IterationNumber, Time]")
    print(time_results)

    return reduced


if __name__ == "__main__":
    MR = [[10, 2]] #, [50, 5], [100, 10]]
    iterations = 1

    couchdb_username = os.getenv("COUCHDB_USER")
    couchdb_password = os.getenv("COUCHDB_PASSWORD")
    couchdb_database = os.getenv("COUCHDB_DATABASE")
    couchdb_host = os.getenv("COUCHDB_HOST")
    # Connect to CouchDB
    couch_db = couchdb.Server(f"http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/")
    dbs = requests.get(f'http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/_all_dbs')

    db = couch_db[couchdb_database]

    dataframe = get_documents_cdb()

    #import dataframe from csv
    #dataframe = pd.read_csv('/energy_large.csv')

    reduce_result = mapReduce(dataframe)
    #print(reduce_result)


    # dump results back to database
    for i in reduce_result:
        docs = json.dumps({'docs': i})
        couchdb_database = MapReduceResults
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = f'http://{couchdb_username}:{couchdb_password}@{couchdb_host}:30009/{couchdb_database}/_bulk_docs'
        req = requests.post(url, headers=headers, data=docs)





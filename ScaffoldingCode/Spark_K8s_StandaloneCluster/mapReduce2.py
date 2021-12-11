
from spark.dataframe import SparkSession




spark = SparkSession\
    .builder\
    .appName("Cloudant Spark SQL Example in Python using dataframes")\
    .config("cloudant.host","ACCOUNT.cloudant.com")\
    .config("cloudant.username", "USERNAME")\
    .config("cloudant.password","PASSWORD")\
    .config("jsonstore.rdd.partitions", 8)\
    .getOrCreate()

# ***1. Loading dataframe from Cloudant db
df = spark.read.load("n_airportcodemapping", "org.apache.bahir.cloudant")
df.cache()
df.printSchema()
df.filter(df.airportName >= 'Moscow').select("_id",'airportName').show()
df.filter(df._id >= 'CAA').select("_id",'airportName').show()	
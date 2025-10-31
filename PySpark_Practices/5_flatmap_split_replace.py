import os
import sys
import urllib.request
import ssl
from collections import namedtuple
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)


python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['HADOOP_HOME'] = os.path.abspath('hadoop')
os.environ['JAVA_HOME'] = r'C:\Users\HP\.jdks\corretto-1.8.0_462'        #  <----- 🔴JAVA PATH🔴


#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars file:///C:/Users/HP/jdbcconnector/mariadb-java-client-3.5.6.jar pyspark-shell'

conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()

print("====Spark Session Created====")
#================================================ Main Code ======================================= #

print()


lststates = ["State->TN~City->Chennai","State->KA~City->Bangalore"]
print("====RAW DATA=====")
print(lststates)
print()


rddstates = sc.parallelize(lststates)
print("=====RDD DATA====")
print(rddstates.collect())
print()


flatstates = rddstates.flatMap(lambda x: x.split("~"))
print("====Flatten Data=====")
print(flatstates.collect())
print()


statesdata = flatstates.filter(lambda x: 'State' in x)
print("====  STATES  =====")
print(statesdata.collect())
print()


citydata = flatstates.filter(lambda x: 'City' in x)
print("====  CITIES  =====")
print(citydata.collect())
print()


finalstate = statesdata.map(lambda x: x.replace("State->",""))
print("===== State Initial ======")
print(finalstate.collect())
print()


finalcity = citydata.map(lambda x: x.replace("City->",""))
print("===== City Initial ======")
print(finalcity.collect())
print()
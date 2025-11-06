import os
import sys
import urllib.request
import ssl
from collections import namedtuple
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number
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


data = [
    ("Sunny","CH",10),
    ("Sunny","CH",15),
    ("Roy","BLR",5),
    ("David","CH",20),
    ("Sunny","HY",15),
    ("Roy","BLR",10),
    ("David","HY",10),
]

columns = ["Name","Address","Amount"]
df = spark.createDataFrame(data, columns)
df.show()
print()


print("=== Sum of amount by name===")
sumdf = df.groupBy("Name").agg(sum("Amount").alias("Total_Amount"))
sumdf.show()


print("====Sum of amount by count of appearence===")
countdf = df.groupBy("Name").agg(sum("Amount").alias("Total"),count("Amount").alias("Count"))
countdf.show()


print("===Average====")
avgdf = df.groupBy("Name").agg(avg("Amount").alias("Average"))
avgdf.show()
print()

print("===Collect List===")
listdf = df.groupBy("Name","Address").agg(collect_list("Amount").alias("List of Amount"))
listdf.show()
print()


print("====Collect Set====")
setdf = df.groupBy("Name").agg(collect_set("Amount").alias("Set of Amount"))
setdf.show()
print()
import os
import urllib.request
import ssl
from collections import namedtuple

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)


# ======================================================================================

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
import os
import urllib.request
import ssl

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['JAVA_HOME'] = r'C:\Users\HP\.jdks\corretto-1.8.0_462'        #  <----- 🔴JAVA PATH🔴
######################🔴🔴🔴##################################

#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'


conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()

spark.read.format("csv").load("data/test.txt").toDF("Success").show(20, False)


##################🔴🔴🔴🔴🔴🔴 -> DONT TOUCH ABOVE CODE -- TYPE BELOW ####################################


print("==========Reading File1 data==========")

data = sc.textFile("file2.txt")
print()
data.foreach(print)
print()


print("=====Filter Gymnastic data=====")
gymfill = data.filter(lambda x: 'Gymnastics' in x)
gymfill.foreach(print)
print()


print("=====Assign Column======")
splitdata = data.map(lambda x: x.split(","))
columns = namedtuple('columns',field_names= ['txnno','tdate','custno','amount','category','product','city','state','spendby'])
coldata = splitdata.map(lambda x: columns(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
coldata.foreach(print)
print()


print("====Convert to Dataframe=====")
df = coldata.toDF()
df.show(10)

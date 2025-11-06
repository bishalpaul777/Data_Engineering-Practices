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

print("====Complex Data Structure and Array=====")

df = spark.read.format("json").option("multiline","true").load(r"rm.json")
df.printSchema()
print()


arr1 = df.selectExpr(
    "nationality",
    "explode(results) as results",
    "seed",
    "version"
)
arr1.printSchema()
print()

str1 = arr1.selectExpr(
    "nationality",
    "results.user",
    "seed",
    "version"
)
str1.printSchema()
print()


str2 = str1.selectExpr(
    "nationality",
    "user.cell",
    "user.dob",
    "user.email",
    "user.gender",
    "user.location.city",
    "user.location.state",
    "user.location.street",
    "user.location.zip",
    "user.md5",
    "user.name.first",
    "user.name.last",
    "user.name.title",
    "user.password",
    "user.phone",
    "user.picture.large",
    "user.picture.medium",
    "user.picture.thumbnail",
    "user.registered",
    "user.salt",
    "user.sha1",
    "user.sha256",
    "user.sha256",
    "user.username",
    "seed",
    "version"
)
str2.show()
str2.printSchema()
print()
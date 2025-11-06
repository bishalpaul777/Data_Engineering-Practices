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
    ("001", "Raj Sharma",  "Sales",    45000, 5000,  "2021-03-15", "Delhi"),
    ("002", "Anjali Verma","Sales",       52000, 7000,  "2020-06-10", "Mumbai"),
    ("003", "Rohan Das",   "IT",       75000, 12000, "2019-09-23", "Bangalore"),
    ("004", "Priya Nair",  "HR",  68000, 8000,  "2022-01-12", "Chennai"),
    ("005", "Karan Mehta", "IT",       80000, 15000, "2018-07-01", "Pune"),
    ("006", "Sneha Iyer",  "Sales",    47000, 4000,  "2023-05-05", "Delhi"),
    ("007", "Abhay Singh", "HR",       49000, 3000,  "2021-11-20", "Mumbai"),
    ("008", "Meena Joshi", "Finance",  72000, 6000,  "2020-02-18", "Bangalore"),
    ("009", "Vikram Rao",  "IT",       67000, 7000,  "2021-09-30", "Chennai"),
    ("010", "Neha Kapoor", "Finance",    52000, 9000,  "2022-04-08", "Pune"),
]

column = ["Id","Name","Department","Salary","Bonus","Date","City"]
df = spark.createDataFrame(data, column)
df.show()
print()


realdata = df.withColumn("Salary",expr("Salary+Bonus as Salary" )).drop("Bonus")
realdata.show()
print()


secondspec = Window.partitionBy("Department").orderBy(col("Salary").desc())
rankit = realdata.withColumn("Rank", dense_rank().over(secondspec))
fildf = rankit.filter("rank == 2").drop("Rank")
fildf.show()


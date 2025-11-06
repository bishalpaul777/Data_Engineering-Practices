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



emp_data = [
    (101, "Raj Sharma", "", 45000, "Delhi"),
    (102, "Anjali Verma", "D2", 52000, "Mumbai"),
    (103, "Rohan Das", "D3", 75000, "Bangalore"),
    (104, "Priya Nair", "D4", 68000, "Chennai"),
    (105, "Karan Mehta", "D3", 80000, "Pune"),
    (106, "Sneha Iyer", "", 47000, "Delhi"),
    (107, "Abhay Singh", "D2", 49000, "Mumbai"),
    (108, "Meena Joshi", "D4", 72000, "Bangalore"),
    (109, "Vikram Rao", "D3", 67000, "Chennai"),
    (110, "Neha Kapoor", "", 52000, "Pune"),
]

dept_data = [
    ("D1", "Sales", "Ramesh Patil", "Delhi"),
    ("D2", "HR", "Sunita Jain", "Mumbai"),
    ("D3", "IT", "Rahul Bansal", "Bangalore"),
    ("D4", "Finance", "Meera Nair", "Chennai"),
    ("D5", "Marketing", "Pooja Iyer", "Hyderabad"),
]

col1 = ["emp_id", "name", "dept_id", "salary", "city"]
df1 = spark.createDataFrame(emp_data, col1)
print("==== Employee Data ====")
df1.show()
print()


col2 = ["dept_id", "dept_name", "manager" , "location"]
df2 = spark.createDataFrame(dept_data, col2)
print("==== Department Data ====")
df2.show()
print()


injoin = df1.join(df2,["dept_id"],"inner").select("name","dept_name","manager")
print("===Inner Join====")
injoin.show()
print()


leftjoin = df1.join(df2, ["dept_id"],"left").select("name","dept_name")
print("==== Left Join=====")
leftjoin.show()
print()


rightjoin = df1.join(df2, "dept_id", "right")
print("==== Right Join=====")
rightjoin.show()
print()


semijoin = df1.join(df2,"dept_id", "semi")
print("====Semi join to print valid department holder employees")
semijoin.show()


antijoin = df2.join(df1, "dept_id","anti").select("dept_name")
print("===Anti join will print the department which have no employees====")
antijoin.show()
print()
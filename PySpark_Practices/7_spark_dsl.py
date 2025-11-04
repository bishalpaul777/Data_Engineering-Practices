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
print("====Main DataFrame=====")

data = [
    ("001", "Electronics", "Mobile Phone", 25000, "2025-01-10"),
    ("002", "Electronics", "Laptop", 72000, "2025-02-14"),
    ("003", "Grocery", "Rice Bag", 1200, "2025-02-15"),
    ("004", "Grocery", "Cooking Oil", 900, "2025-03-05"),
    ("005", "Fashion", "T-Shirt", 800, "2025-03-21"),
    ("006", "Fashion", "Jeans", 2200, "2025-03-22"),
    ("007", "Furniture", "Chair", 3500, "2025-04-01"),
    ("008", "Furniture", "Table", 5800, "2025-04-10"),
    ("009", "Electronics", "Headphones", 1500, "2025-05-03"),
    ("010", "Grocery", "Milk Packet", 60, "2025-05-05"),
]

columns = ['Id','Category','Product','Amount','Date']
df = spark.createDataFrame(data,columns)
df.show()

print("====DSL Start====")
print()

print("=====Showing only Electronics data====")
eledf = df.filter("Category = 'Electronics'")
eledf.show()
print()


print("====Amount greater than 5000====")
amtdf = df.filter("Amount > 5000")
amtdf.show()
print()


print("===Electronics or Furniture whose amount > 2000====")
elefurdf = df.filter("amount > 2000 AND (category = 'Electronics' or category = 'Furniture')")
elefurdf.show()
print()


print("====Sorting by amount ascending order =====")
sortdf = df.orderBy(df.Amount.asc())
sortdf.show()
print()


print("===UPPER Product===")
uppdf = df.selectExpr("Id","Category","upper(Product) as Product","Amount","Date")
uppdf.show()
print()


print("====Cast Id====")
castdf = df.selectExpr("cast(Id as int) as Id")
castdf.show()
print()


print("====Adding 1200 to Grocery Item, 1000 to Furniture and 500 to rest====")
addf = df.selectExpr("Id",
                     "Category",
                     "Product",
                     "Case when Category = 'Grocery' then Amount + 1200 when Category = ' Furniture' then Amount + 1000 else Amount + 500 end as Amount",
                     "split(Date,'-')[0] as Year")
addf.show()
print()


print("===Total and Average for Each Category====")
totalavg = df.groupBy("Category").agg(sum("Amount").alias("Total_Amount"), round(avg("Amount"),2).alias("Average_Amount"))
totalavg.show()
print()


print("====Top 3 Highest Amount Product====")
topdf = df.orderBy(df.Amount.desc()).limit(3)
topdf.show()
print()


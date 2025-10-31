import os
import urllib.request
import ssl
from collections import namedtuple

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)

os.environ['HADOOP_HOME'] = os.path.abspath('hadoop')
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
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars file:///C:/Users/HP/jdbcconnector/mariadb-java-client-3.5.6.jar pyspark-shell'


conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()

spark.read.format("csv").load("data/test.txt").toDF("Success").show(20, False)


##################🔴🔴🔴🔴🔴🔴 -> DONT TOUCH ABOVE CODE -- TYPE BELOW ####################################


print()

print("=====CSV to Dataframe======")
csvdf = spark.read.format("csv").option("header","true").load("usdata.csv")
csvdf.show()
print()


print("======Json ton Dataframe======")
jsondf = spark.read.format("json").load("file4.json")
jsondf.show()
print()


print("=====Parquet to Dataframe======")
parqdf = spark.read.load("file5.parquet")
parqdf.show()
print()


print("=====ORC to Dataframe")
orcdf = spark.read.format("orc").load("data.orc")
orcdf.show()
print()



# print("=====SQL to Dataframe=====")
#
# sqldf = (
#     spark.read
#     .format("jdbc")
#     .option("url", "jdbc:mariadb://localhost:3306/movies")
#     .option("driver", "org.mariadb.jdbc.Driver")
#     .option("user", "root")
#     .option("password", "")
#     .option("query", "SELECT CAST(id AS CHAR) AS id, name, director, CAST(date AS CHAR) AS date FROM movie_details")
#     .load()
# )
#
#
# sqldf = sqldf.withColumn("id", col("id").cast("int"))
# sqldf = sqldf.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
# sqldf.printSchema()
# sqldf.show()



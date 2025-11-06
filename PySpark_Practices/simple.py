import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("simple").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
data = [
    (1, "Alice"),
    (2, "John")
]

colmn = ["Id","Name"]
df = spark.createDataFrame(data,colmn)
df.show()
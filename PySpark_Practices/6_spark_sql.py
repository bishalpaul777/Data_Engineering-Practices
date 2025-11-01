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


data = [
    [115, "Oscar Wright",     "Finance",   "Accountant",        60000, 4, "Houston"],
    [107, "George Brown",     "IT",        "Data Engineer",     90000, 5, "Austin"],
    [113, "Megan Brooks",     "HR",        "HR Executive",      60000, 2, "Denver"],
    [110, "Jane Adams",       "Marketing", "SEO Specialist",    60000, 3, "Boston"],
    [118, "Ryan Foster",      "IT",        "Software Tester",   70000, 2, "San Diego"],
    [102, "Bob Smith",        "HR",        "HR Executive",      55000, 2, "Boston"],
    [119, "Sophia Allen",     "IT",        "Data Engineer",     90000, 6, "Dallas"],
    [111, "Kevin Harris",     "Sales",     "Sales Executive",   58000, 2, "Miami"],
    [116, "Paula Martin",     "Finance",   "Finance Manager",   85000, 8, "New York"],
    [120, "Tom Clark",        "IT",        "Software Tester",   60000, 4, "Seattle"],
    [101, "Alice Johnson",    "HR",        "HR Executive",      55000, 3, "New York"],
    [108, "Hannah Wilson",    "IT",        "Software Tester",   70000, 3, "Seattle"],
    [112, "Laura Scott",      "Sales",     "Sales Executive",   58000, 3, "Miami"],
    [117, "Quentin Lee",      "Sales",     "Sales Executive",   58000, 4, "Chicago"],
    [103, "Charlie Evans",    "Finance",   "Accountant",        60000, 4, "Chicago"],
    [105, "Ethan White",      "Finance",   "Finance Manager",   85000, 7, "New York"],
    [109, "Ian Thomas",       "Marketing", "SEO Specialist",    65000, 4, "Boston"],
    [106, "Fiona Green",      "IT",        "Data Engineer",     90000, 6, "San Francisco"],
    [104, "Diana Carter",     "Finance",   "Accountant",        60000, 5, "Chicago"],
    [114, "Nathan Reed",      "Marketing", "SEO Specialist",    65000, 5, "New York"]
]


print("=====Data Frame======")

schema = ["Id","Name","Department","Role","Salary","Experience","Location"]
df = spark.createDataFrame(data, schema)
df.show()
print()

df.createOrReplaceTempView("sqldf")

print("=====Ascending Order ID=====")
spark.sql("select * from sqldf order by Id asc").show()
print()


print("==== Experience more than 3 Years=====")
spark.sql("select * from sqldf where experience > 4").show()
print()


print("======Count employees by department====")
spark.sql("select Department,count(*) as total_employee from sqldf group by Department ").show()
print()


print("==== Average Salary of Each Department====")
spark.sql("select Department,avg(salary) as Average_Salary from sqldf group by Department").show()
print()


print("==== List of Employee Salary > 70,000=====")
spark.sql("select Name,Salary from sqldf where Salary > 70000").show()
print()


print("==== Min and Max salary by employee and department====")
spark.sql("""
select Name,
Department,
Salary,
Case
when salary = (select max(salary) from sqldf) then 'Highest_Salary'
when salary = (select min(salary) from sqldf) then 'Minimum_Salary'
End as Salary_Type
from sqldf
where salary in ( select max(salary) from sqldf union all select min(salary) from sqldf)

""").show()
print()


print("====Employees by City====")
spark.sql("select Location,count(*) as Total_Employee from sqldf group by Location ").show()
print()


print("====Distinct Job roles=====")
spark.sql("""
select * from
( select *, Row_Number() over (partition by Role order by Id) as rn from sqldf) temp
where rn = 1
""").drop("rn").show()
print()


print("==== List of Employees salary equal to any accountant salary====")
spark.sql("""
select * from sqldf
where Salary IN 
( select distinct Salary from sqldf
where Role = 'Accountant')
""").show()
print()


# Show the top 3 highest-paid employees.
#
# Find the average experience of employees in the “Finance” department.
#
# List employees who work in Boston or New York.
#
# Count how many unique job roles exist in the IT department.
#
# Display employees ordered by salary descending and experience ascending.
#
# Find the department with the highest average salary.
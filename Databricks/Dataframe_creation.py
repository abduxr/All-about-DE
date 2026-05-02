from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()


data=[('1','Abdul')]
schema='ID String, Name String'

df = spark.createDataFrame(data,schema)
df.show()

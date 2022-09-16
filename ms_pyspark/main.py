from pyspark.sql import SparkSession

spark= SparkSession.builder\
    .master("spark://127.0.0.1:7077")\
    .appName("sparkExample")\
    .getOrCreate()


sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100 + 1))
rdd.sum()

#df=spark.read.csv("./files/001.csv",header=True)
#df.show()

spark.stop()

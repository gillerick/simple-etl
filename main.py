import pyspark

spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL simple example") \
    .config('spark.driver.extraClassPath', "postgresql-42.5.0.jar") \
    .getOrCreate()

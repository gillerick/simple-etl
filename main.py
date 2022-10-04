import pyspark

spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL simple example") \
    .config('spark.driver.extraClassPath', "postgresql-42.5.0.jar") \
    .getOrCreate()

movies_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/movies_db") \
    .option("dbtable", "movies") \
    .option("user", "user") \
    .option("password", "pass") \
    .option("driver", "org.postgresql.Driver") \
    .load()

if __name__ == "__main__":
    print(movies_df.show())
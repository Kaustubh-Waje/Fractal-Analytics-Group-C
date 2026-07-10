import redis
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    ) \
    .config(
        "spark.jars",
        "/home/kaustubh/task1/postgresql-42.7.3.jar"
    ) \
    .getOrCreate()

df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "invoice-topic") \
    .option("startingOffsets", "earliest") \
    .load()

schema = StructType() \
    .add("vendor", StringType()) \
    .add("amount", IntegerType()) \
    .add("status", StringType())

decoded_df = df.selectExpr(
    "CAST(value AS STRING) as message"
)

json_df = decoded_df.select(
    from_json(col("message"), schema).alias("data")
)

final_df = json_df.select("data.*")

final_df.show()
final_df = final_df.filter(
    col("vendor").isNotNull()
)
final_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5433/procurement") \
    .option("dbtable", "kafka_invoices") \
    .option("user", "kaustubh") \
    .option("password", "1234") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()

print("Data written to PostgreSQL!")
r = redis.Redis(
    host="localhost",
    port=6380,
    decode_responses=True
)

r.delete("all_invoices")
print("Redis cache cleared!")
spark.stop()      

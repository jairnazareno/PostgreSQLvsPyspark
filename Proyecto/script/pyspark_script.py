1.- CARGA INCIAL

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkApp").getOrCreate()

rdd = sc.textFile("/dataset/yahoo-symbols-201709.csv")

header = rdd.first()  
data = rdd.filter(lambda row: row != header).map(lambda row: row.split(","))

columns = header.split(",")
df = spark.createDataFrame(data, schema=columns)

import time

start_time = time.time()

rows = df.limit(100000).collect()

end_time = time.time()

print(f"Tiempo de ejecución para recolectar 100,000 filas: {end_time - start_time} segundos")

----------------------------------------------------------------------------------------------

2.- INSERCIÓN DE DATOS

from pyspark.sql import Row
import time

extra_data = [Row(ticker=f"SYM{i}", 
                  name=f"Name{i}", 
                  exchange=f"EX", 
                  category_name=f"Category", 
                  country=f"USA") for i in range(10001, 20001)]

extra_df = spark.createDataFrame(extra_data)

start_time = time.time()

df_combined = df.union(extra_df)

end_time = time.time()

print(f"Tiempo para añadir 10,000 filas: {end_time - start_time:.4f} segundos")

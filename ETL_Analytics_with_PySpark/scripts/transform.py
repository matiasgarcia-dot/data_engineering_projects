from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc, when
import os

# Crear sesión de Spark
spark = SparkSession.builder.appName("CarSalesAnalysis").getOrCreate()

# Cargar el CSV con PySpark
df = spark.read.csv("data_initial/car_sales.csv", header=True, inferSchema=True)

# Renombrar columnas para mayor claridad
df = df.withColumnRenamed("year", "manufacture_year") \
       .withColumnRenamed("make", "brand") \
       .withColumnRenamed("model", "car_model") \
       .withColumnRenamed("transmission", "transmission_type") \
       .withColumnRenamed("odometer", "mileage") \
       .withColumnRenamed("sellingprice", "sale_price") \
       .withColumnRenamed("saledate", "sale_date")

# Seleccionar solo las columnas necesarias
df = df.select("brand", "transmission_type", "manufacture_year", "car_model", "mileage", "sale_price", "sale_date")

# Eliminar filas con valores nulos
df = df.dropna()

# Contar las marcas más vendidas
top_brands = (df.groupBy("brand")
                .agg(count("brand").alias("total_sales"))
                .orderBy(desc("total_sales")))

# Contar la cantidad de autos automáticos y manuales por marca
transmission_count = (df.groupBy("brand")
                      .agg(
                          count(when(col("transmission_type") == "automatic", True)).alias("automatic_count"),
                          count(when(col("transmission_type") == "manual", True)).alias("manual_count")
                      )
                      .orderBy(desc("automatic_count"), desc("manual_count")))

# Mostrar resultados
top_brands.show()
transmission_count.show()

# Guardar los datos transformados 
output_dir = "data_transformed"
os.makedirs(output_dir, exist_ok=True)

top_brands.write.mode("overwrite").option("header", "true").csv(f"{output_dir}/top_brands")
transmission_count.write.mode("overwrite").option("header", "true").csv(f"{output_dir}/transmission_count")

print("✅ Transformación completada y datos guardados en formato CSV")

# Cerrar sesión de Spark
spark.stop()

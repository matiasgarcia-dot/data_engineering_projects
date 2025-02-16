from pyspark.sql import SparkSession

def extract_data(file_path):
    spark = SparkSession.builder.appName("CarSalesETL").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    df.show()
    return df, spark

if __name__ == "__main__":
    file_path = "data_initial/car_sales.csv"
    df, spark = extract_data(file_path)

    # Guardar los datos en formato Parquet para el siguiente paso
    # Guardar los datos en formato CSV para el siguiente paso
    df.write.mode("overwrite").option("header", "true").csv("data_extract/extracted_data")
    
    print("✅ Datos extraídos y guardados en CSV.")


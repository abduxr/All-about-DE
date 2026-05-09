# ==========================================
# NOTEBOOK: 01_landing_to_bronze
# PURPOSE:
#   Raw CSV → Bronze Delta Layer
# ==========================================

# ------------------------------------------
# STEP 1 — IMPORTS
# ------------------------------------------

from pyspark.sql.functions import (
    current_timestamp,
    col
)

# ------------------------------------------
# STEP 2 — CREATE DATABASE
# ------------------------------------------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retail
""")

# ------------------------------------------
# STEP 3 — DATASETS LIST
# ------------------------------------------

datasets = [
    "customers",
    "products",
    "stores",
    "orders",
    "payments"
]

# ------------------------------------------
# STEP 4 — LOOP THROUGH DATASETS
# ------------------------------------------

for table in datasets:

    print(f"\nProcessing table: {table}")

    # --------------------------------------
    # SOURCE CSV PATH
    # --------------------------------------

    path = f"/Volumes/workspace/master/filestore/retails/raw/{table}.csv"

    # --------------------------------------
    # READ CSV FILE
    # --------------------------------------

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(path)

    # --------------------------------------
    # ADD METADATA COLUMNS
    # --------------------------------------

    df = df.withColumn(
        "ingestion_time",
        current_timestamp()
    ).withColumn(
        "source_file",
        col("_metadata.file_path")
    )

    # --------------------------------------
    # BRONZE DELTA STORAGE PATH
    # --------------------------------------

    bronze_path = f"/Volumes/workspace/master/filestore/retails/bronze/{table}"

    # --------------------------------------
    # WRITE DELTA FILES
    # --------------------------------------

    df.write.format("delta") \
        .mode("overwrite") \
        .save(bronze_path)

    print(f"Delta files created at: {bronze_path}")

    # --------------------------------------
    # REGISTER METADATA TABLE
    # --------------------------------------

    spark.sql(f"""
        CREATE OR REPLACE TABLE retail.bronze_{table}
        USING DELTA
        AS
        SELECT *
        FROM delta.`{bronze_path}`
    """)

    print(f"Registered table: retail.bronze_{table}")

# ------------------------------------------
# STEP 5 — VERIFY TABLES
# ------------------------------------------

display(
    spark.sql("SHOW TABLES IN retail")
)
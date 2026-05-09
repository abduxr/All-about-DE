# ==========================================
# NOTEBOOK: 04_scd2_customers
# PURPOSE:
#   Build Customer SCD2 Historical Table
# ==========================================

# ------------------------------------------
# STEP 1 — IMPORTS
# ------------------------------------------

from pyspark.sql.functions import (
    current_date,
    lit,
    current_timestamp
)

# ------------------------------------------
# STEP 2 — CREATE SCHEMA
# ------------------------------------------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retail
""")

# ------------------------------------------
# STEP 3 — READ SILVER CUSTOMERS
# ------------------------------------------

customers_df = spark.table(
    "retail.silver_customers"
)

print("Silver customers loaded")

display(customers_df.limit(5))

# ------------------------------------------
# STEP 4 — ADD SCD2 COLUMNS
# ------------------------------------------

scd2_df = customers_df \
    .withColumn(
        "effective_start_date",
        current_date()
    ) \
    .withColumn(
        "effective_end_date",
        lit(None).cast("date")
    ) \
    .withColumn(
        "is_current",
        lit(True)
    ) \
    .withColumn(
        "scd_created_time",
        current_timestamp()
    )

print("SCD2 columns added")

display(scd2_df.limit(5))

# ------------------------------------------
# STEP 5 — DEFINE SCD2 PATH
# ------------------------------------------

scd2_path = "/Volumes/workspace/master/filestore/retails/gold/customers_scd2"

# ------------------------------------------
# STEP 6 — WRITE SCD2 DELTA
# ------------------------------------------

scd2_df.write.format("delta") \
    .mode("overwrite") \
    .save(scd2_path)

print(f"SCD2 Delta written: {scd2_path}")

# ------------------------------------------
# STEP 7 — REGISTER SCD2 TABLE
# ------------------------------------------

spark.sql(f"""
    CREATE OR REPLACE TABLE retail.customers_scd2
    USING DELTA
    AS
    SELECT *
    FROM delta.`{scd2_path}`
""")

print("Registered: retail.customers_scd2")

# ------------------------------------------
# STEP 8 — VERIFY TABLE
# ------------------------------------------

display(
    spark.sql("""
        SELECT *
        FROM retail.customers_scd2
        LIMIT 10
    """)
)

# ------------------------------------------
# STEP 9 — VERIFY SCD2 STATUS
# ------------------------------------------

display(
    spark.sql("""
        SELECT
            customer_id,
            first_name,
            city,
            loyalty_tier,
            effective_start_date,
            effective_end_date,
            is_current
        FROM retail.customers_scd2
    """)
)

print("SCD2 Customer Dimension Created Successfully")
# ==========================================
# NOTEBOOK: 02_bronze_to_silver
# PURPOSE:
#   Bronze → Silver Layer Processing
# ==========================================

# ------------------------------------------
# STEP 1 — IMPORTS
# ------------------------------------------

from pyspark.sql.functions import (
    col,
    to_date,
    current_timestamp
)

# ------------------------------------------
# STEP 2 — CREATE SCHEMA
# ------------------------------------------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retail
""")

# ------------------------------------------
# STEP 3 — DATASETS
# ------------------------------------------

datasets = [
    "customers",
    "products",
    "stores",
    "orders",
    "payments"
]

# ------------------------------------------
# STEP 4 — PROCESS EACH TABLE
# ------------------------------------------

for table in datasets:

    try:

        print(f"\n===================================")
        print(f"Processing Silver Layer: {table}")
        print(f"===================================")

        # --------------------------------------
        # READ BRONZE TABLE
        # --------------------------------------

        bronze_df = spark.table(
            f"retail.bronze_{table}"
        )

        print("Bronze Count:")
        print(bronze_df.count())

        # --------------------------------------
        # REMOVE DUPLICATES
        # --------------------------------------

        silver_df = bronze_df.dropDuplicates()

        # ======================================
        # CUSTOMERS TABLE
        # ======================================

        if table == "customers":

            silver_df = silver_df \
                .withColumn(
                    "age",
                    col("age").cast("int")
                ) \
                .withColumn(
                    "signup_date",
                    to_date(col("signup_date"))
                )

            silver_df = silver_df.na.drop(
                subset=["customer_id"]
            )

        # ======================================
        # PRODUCTS TABLE
        # ======================================

        elif table == "products":

            silver_df = silver_df \
                .withColumn(
                    "unit_cost",
                    col("unit_cost").cast("double")
                ) \
                .withColumn(
                    "selling_price",
                    col("selling_price").cast("double")
                ) \
                .withColumn(
                    "stock_quantity",
                    col("stock_quantity").cast("int")
                ) \
                .withColumn(
                    "rating",
                    col("rating").cast("double")
                )

        # ======================================
        # STORES TABLE
        # ======================================

        elif table == "stores":

            print("Before casting:")
            print(silver_df.dtypes)

            silver_df = silver_df.withColumn(
                "floor_area_sqft",
                col("floor_area_sqft").cast("double")
            )

            silver_df = silver_df.na.drop(
                subset=["store_id"]
            )

            print("After casting:")
            print(silver_df.dtypes)

        # ======================================
        # ORDERS TABLE
        # ======================================

        elif table == "orders":

            print("Before casting:")
            print(silver_df.dtypes)

            silver_df = silver_df \
                .withColumn(
                    "quantity",
                    col("quantity").cast("int")
                ) \
                .withColumn(
                    "unit_price",
                    col("unit_price").cast("double")
                ) \
                .withColumn(
                    "discount",
                    col("discount").cast("double")
                ) \
                .withColumn(
                    "tax",
                    col("tax").cast("double")
                ) \
                .withColumn(
                    "shipping_cost",
                    col("shipping_cost").cast("double")
                ) \
                .withColumn(
                    "total_amount",
                    col("total_amount").cast("double")
                ) \
                .withColumn(
                    "delivery_days",
                    col("delivery_days").cast("int")
                )

            silver_df = silver_df.na.drop(
                subset=[
                    "quantity",
                    "total_amount"
                ]
            )

            silver_df = silver_df.filter(
                col("quantity") > 0
            )

            silver_df = silver_df.filter(
                col("total_amount") > 0
            )

            print("After casting:")
            print(silver_df.dtypes)

        # ======================================
        # PAYMENTS TABLE
        # ======================================

        elif table == "payments":

            silver_df = silver_df \
                .withColumn(
                    "amount_paid",
                    col("amount_paid").cast("double")
                )

            silver_df = silver_df.filter(
                col("amount_paid") > 0
            )

        # --------------------------------------
        # ADD SILVER METADATA
        # --------------------------------------

        silver_df = silver_df.withColumn(
            "silver_processed_time",
            current_timestamp()
        )

        # --------------------------------------
        # DISPLAY SAMPLE DATA
        # --------------------------------------

        display(
            silver_df.limit(5)
        )

        # --------------------------------------
        # SILVER STORAGE PATH
        # --------------------------------------

        silver_path = f"/Volumes/workspace/master/filestore/retails/silver/{table}"

        print(f"Writing to: {silver_path}")

        # --------------------------------------
        # WRITE SILVER DELTA
        # --------------------------------------

        silver_df.write.format("delta") \
            .mode("overwrite") \
            .save(silver_path)

        print(f"Silver Delta written successfully")

        # --------------------------------------
        # REGISTER SILVER TABLE
        # --------------------------------------

        spark.sql(f"""
            CREATE OR REPLACE TABLE retail.silver_{table}
            USING DELTA
            AS
            SELECT *
            FROM delta.`{silver_path}`
        """)

        print(f"Registered: retail.silver_{table}")

    except Exception as e:

        print(f"\nERROR OCCURRED IN TABLE: {table}")
        print(str(e))

# ------------------------------------------
# STEP 5 — VERIFY TABLES
# ------------------------------------------

print("\n===================================")
print("ALL REGISTERED TABLES")
print("===================================")

display(
    spark.sql("SHOW TABLES IN retail")
)
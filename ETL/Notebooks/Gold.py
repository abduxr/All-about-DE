# ==========================================
# NOTEBOOK: 03_silver_to_gold
# PURPOSE:
#   Silver → Gold Layer
# ==========================================

# ------------------------------------------
# STEP 1 — IMPORTS
# ------------------------------------------

from pyspark.sql.functions import (
    sum,
    count,
    avg,
    round,
    current_timestamp
)

# ------------------------------------------
# STEP 2 — CREATE SCHEMA
# ------------------------------------------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retail
""")

# ==========================================
# STEP 3 — LOAD SILVER TABLES
# ==========================================

orders_df = spark.table("retail.silver_orders")

customers_df = spark.table("retail.silver_customers")

products_df = spark.table("retail.silver_products")

stores_df = spark.table("retail.silver_stores")

payments_df = spark.table("retail.silver_payments")

# ==========================================
# GOLD 1 — CUSTOMER REVENUE
# ==========================================

customer_revenue_df = orders_df.groupBy(
    "customer_id"
).agg(
    round(sum("total_amount"), 2).alias("total_revenue"),
    count("order_id").alias("total_orders"),
    round(avg("total_amount"), 2).alias("avg_order_value")
)

customer_revenue_df = customer_revenue_df.withColumn(
    "gold_processed_time",
    current_timestamp()
)

display(customer_revenue_df)

# ------------------------------------------
# WRITE GOLD DELTA
# ------------------------------------------

customer_revenue_path = "/Volumes/workspace/master/filestore/retails/gold/customer_revenue"

customer_revenue_df.write.format("delta") \
    .mode("overwrite") \
    .save(customer_revenue_path)

# ------------------------------------------
# REGISTER TABLE
# ------------------------------------------

spark.sql(f"""
CREATE OR REPLACE TABLE retail.gold_customer_revenue
USING DELTA
AS
SELECT *
FROM delta.`{customer_revenue_path}`
""")

print("Created: retail.gold_customer_revenue")

# ==========================================
# GOLD 2 — PRODUCT SALES
# ==========================================

product_sales_df = orders_df.join(
    products_df,
    "product_id"
).groupBy(
    "product_id",
    "product_name",
    "category"
).agg(
    round(sum("total_amount"), 2).alias("total_sales"),
    count("order_id").alias("total_orders")
)

product_sales_df = product_sales_df.withColumn(
    "gold_processed_time",
    current_timestamp()
)

display(product_sales_df)

# ------------------------------------------
# WRITE GOLD DELTA
# ------------------------------------------

product_sales_path = "/Volumes/workspace/master/filestore/retails/gold/product_sales"

product_sales_df.write.format("delta") \
    .mode("overwrite") \
    .save(product_sales_path)

# ------------------------------------------
# REGISTER TABLE
# ------------------------------------------

spark.sql(f"""
CREATE OR REPLACE TABLE retail.gold_product_sales
USING DELTA
AS
SELECT *
FROM delta.`{product_sales_path}`
""")

print("Created: retail.gold_product_sales")

# ==========================================
# GOLD 3 — STORE PERFORMANCE
# ==========================================

store_perf_df = orders_df.join(
    stores_df,
    "store_id"
).groupBy(
    "store_id",
    "store_name",
    "region"
).agg(
    round(sum("total_amount"), 2).alias("store_revenue"),
    count("order_id").alias("total_orders")
)

store_perf_df = store_perf_df.withColumn(
    "gold_processed_time",
    current_timestamp()
)

display(store_perf_df)

# ------------------------------------------
# WRITE GOLD DELTA
# ------------------------------------------

store_perf_path = "/Volumes/workspace/master/filestore/retails/gold/store_performance"

store_perf_df.write.format("delta") \
    .mode("overwrite") \
    .save(store_perf_path)

# ------------------------------------------
# REGISTER TABLE
# ------------------------------------------

spark.sql(f"""
CREATE OR REPLACE TABLE retail.gold_store_performance
USING DELTA
AS
SELECT *
FROM delta.`{store_perf_path}`
""")

print("Created: retail.gold_store_performance")

# ==========================================
# GOLD 4 — CHANNEL SALES
# ==========================================

channel_sales_df = orders_df.groupBy(
    "channel"
).agg(
    round(sum("total_amount"), 2).alias("channel_revenue"),
    count("order_id").alias("total_orders")
)

channel_sales_df = channel_sales_df.withColumn(
    "gold_processed_time",
    current_timestamp()
)

display(channel_sales_df)

# ------------------------------------------
# WRITE GOLD DELTA
# ------------------------------------------

channel_sales_path = "/Volumes/workspace/master/filestore/retails/gold/channel_sales"

channel_sales_df.write.format("delta") \
    .mode("overwrite") \
    .save(channel_sales_path)

# ------------------------------------------
# REGISTER TABLE
# ------------------------------------------

spark.sql(f"""
CREATE OR REPLACE TABLE retail.gold_channel_sales
USING DELTA
AS
SELECT *
FROM delta.`{channel_sales_path}`
""")

print("Created: retail.gold_channel_sales")

# ==========================================
# GOLD 5 — PAYMENT SUMMARY
# ==========================================

payment_summary_df = payments_df.groupBy(
    "payment_method",
    "payment_status"
).agg(
    round(sum("amount_paid"), 2).alias("total_payment_amount"),
    count("payment_id").alias("total_transactions")
)

payment_summary_df = payment_summary_df.withColumn(
    "gold_processed_time",
    current_timestamp()
)

display(payment_summary_df)

# ------------------------------------------
# WRITE GOLD DELTA
# ------------------------------------------

payment_summary_path = "/Volumes/workspace/master/filestore/retails/gold/payment_summary"

payment_summary_df.write.format("delta") \
    .mode("overwrite") \
    .save(payment_summary_path)

# ------------------------------------------
# REGISTER TABLE
# ------------------------------------------

spark.sql(f"""
CREATE OR REPLACE TABLE retail.gold_payment_summary
USING DELTA
AS
SELECT *
FROM delta.`{payment_summary_path}`
""")

print("Created: retail.gold_payment_summary")

# ==========================================
# STEP 4 — VERIFY GOLD TABLES
# ==========================================

display(
    spark.sql("SHOW TABLES IN retail")
)
# Databricks notebook source
df = spark.range(1,100)
df.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE samples.tpch.test AS SELECT * FROM df

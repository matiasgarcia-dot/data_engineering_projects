import sqlite3
import pandas as pd

# Load the transformed DataFrame from the CSV file generated in transform.py
df = pd.read_csv("transformed_data.csv")

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect("risk_analysis.db")
cursor = conn.cursor()

# Create a table with the new columns if it does not already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS risk_data (
    risk_value INTEGER,        -- Risk value (integer type)
    date TEXT,                 -- Date of the record (text type)
    daily_variation REAL,      -- Daily variation in risk value (real type)
    percent_change REAL,       -- Percentage change in risk value (real type)
    trend TEXT                 -- Trend: Increase, Decrease, or No Change (text type)
)
""")

# Insert the DataFrame data into the 'risk_data' table
df.to_sql("risk_data", conn, if_exists="append", index=False)

# Verify the data was successfully loaded into the table
cursor.execute("SELECT * FROM risk_data LIMIT 5")  # Select the first 5 rows from the table
rows = cursor.fetchall()  # Fetch the selected rows
for row in rows:
    print(row)  # Print each row to confirm the data

# Close the connection to the SQLite database
conn.close()

# Employee Data Cleaning with SQL 🧹🗃️

This project demonstrates how to clean and normalize a real-world employee dataset using MySQL. It includes handling messy column names, inconsistent values, and data types for better analysis and reporting.

## 📁 Dataset

The dataset used is a CSV file (`data.csv`) that contains employee records with:
- Inconsistent column names
- Mixed gender formats (e.g., "hombre", "mujer")
- Untrimmed strings
- Salaries with `$` and `,`
- Dates in `MM/DD/YYYY` format
- Redundant rows

## 🧪 Goals

- Standardize column names
- Remove duplicate records
- Normalize gender and area fields
- Clean and convert salary to numeric format
- Convert start date to proper `DATE` format
- Drop irrelevant or empty records
- Prepare a clean, query-ready table for analysis

## 🧰 Tech Stack

- **MySQL** (tested in MySQL Workbench)
- SQL scripting
- CSV file import/export

## 📜 How It Works

The cleaning is done entirely with SQL queries. The script includes:

1. Creating a new clean database
2. Fixing malformed headers (e.g., encoding issues)
3. Removing duplicates
4. Normalizing columns (`Gender`, `Area`, etc.)
5. Cleaning string values (trimming whitespace)
6. Converting `salary` and `start_date` to usable formats
7. Dropping empty or invalid rows
8. Creating a stored procedure for querying clean data

## 🚀 How to Use

1. Import `data.csv` into MySQL Workbench as a table named `data`
2. Run the SQL script `cleaning_script.sql`
3. Use the stored procedure `CALL limp();` to preview cleaned data

## 📂 File Structure

```
├── data.csv                # Raw CSV dataset
├── database_clean.sql      # Raw CSV dataset
├── cleaning_script.sql     # Main SQL cleaning script
└── README.md               # Project documentation
```

## 🧠 Lessons Learned

- Importance of column name normalization
- Working with text-to-date conversions in SQL
- Using `REGEXP_REPLACE`, `TRIM`, and `LOWER` to standardize data
- Leveraging temporary tables and stored procedures in MySQL

## 💡 Possible Improvements

- Automate CSV import via Python (e.g., with `pandas` and `SQLAlchemy`)
- Add unit tests for each SQL step (with stored procedures or external tools)
- Visualize cleaned data with a dashboard (e.g., Power BI or Tableau)

---



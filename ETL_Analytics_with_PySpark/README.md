# 🚗 Car Sales Analytics: PySpark + Power BI + ETL

## 📖 Description
This project performs an ETL (Extract, Transform, Load) process using **PySpark** to transform and analyze car sales data (https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data). The transformed data is visualized in **Power BI** through PDF charts and a Power BI template, highlighting best-selling car brands and transmission type analysis (automatic vs. manual).

## ✨ Main Features

- ✅ **Complete ETL Process**: Data extraction, transformation, and loading.
- ✅ **Scalable Data Handling**: Use of **PySpark** for processing large datasets.
- ✅ **Interactive Visualizations**: Data visualization through **Power BI**.
- ✅ **CSV Data Storage**: Transformed data is stored in CSV format for further analysis.

## 📋 Prerequisites

- **Python** (3.x)

If you want to explore the visualizations:
- **Power BI Desktop** (for deeper chart analysis)

## 🚀 Execution Steps

### 1. Clone the Repository

```bash
git clone https://github.com/matiasgarcia-dot/data_engineering_projects.git
cd data_engineering_projects/ETL_ANALYTICS_WITH_PYSPARK
```

### 2. Create a Virtual Environment

#### On **Windows**:
```bash
python -m venv car_sales
.car_sales\Scripts\activate
```

#### On **Linux/Mac**:
```bash
python3 -m venv car_sales
source car_sales/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Environment

If you want to reset the project execution, delete the following folders before running the scripts:

- `data_extract`
- `data_transformed`

### 5. Execution Order

1. Run the **data extraction** script:
   ```bash
   python scripts/extract.py
   ```

2. Run the **data transformation** script:
   ```bash
   python scripts/transform.py
   ```

## 📂 Project Structure

```
📂 ETL_ANALYTICS_WITH_PYSPARK
|
├── 📂 data_initial                    # Raw data before the ETL process
│    └── car_sales.csv                # Original raw CSV file
|
├── 📂 data_extract                    # Data extracted using PySpark
│    └── extracted_data.csv           # Extracted data in CSV format
|
├── 📂 data_transformed                # Transformed data after the ETL process
│    ├── 📂 top_brands                # Best-selling car brands (CSV)
│    └── 📂 transmission_count        # Transmission analysis by brand (CSV)
|
├── 📂 final_analysis                  # Power BI visualization files
│    ├── Analysis_top_brands_sold.pdf                    # Chart of the best-selling car brands (PDF)
│    ├── Analysis_car_transmission_by_brands.pdf         # Transmission analysis by brand (PDF)
│    └── Analysis_top_brands_sold_&_car_transmission.pbit # Power BI file with both visualizations
|
├── 📂 scripts                         # ETL process scripts
│    ├── extract.py                   # Data extraction script
│    └── transform.py                 # Data transformation script
|
├── 📄 README.md                       # Project documentation
└── 📄 requirements.txt                # Virtual environment dependencies
```

## 📊 Output

The output includes:

- **Best-Selling Brands**: A detailed analysis of the top car brands by sales volume.
- **Transmission Analysis**: Insights comparing automatic and manual transmissions.
- **Interactive Dashboard**: Power BI template to interact with the processed data.


## 📧 Contact
For any questions or contributions, feel free to contact **Matias Garcia**.
matisgar32@gmail.com






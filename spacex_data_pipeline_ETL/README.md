# SpaceX ETL Pipeline

This project implements an **ETL (Extract, Transform, Load)** process using SpaceX data. It collects data from the SpaceX API about rockets and rocket launches. This data is processed through three storage layers (**Bronze**, **Silver** and **Gold**) and prepared for analysis.

---

## 📁 Project Structure

```
spacex_data_pipeline_ETL/
├── delta_lake_data/
│    ├── bronze/   # Raw data from APIs
│    ├── silver/   # Cleaned and processed data
│    └── gold/     # Final, enriched dataset
│
├── scripts/
│    ├── extract.py   # Handles data extraction
│    ├── transform.py # Cleans and transforms the data
│    └── load.py      # Loads data into Delta Lake format
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Requirements

- Python 3.x
- Visual Studio Code (or any IDE)

Ensure you have **Python** installed:
```bash
python --version
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/matiasgarcia-dot/data_engineering_projects.git
cd data_engineering_projects/spacex_data_pipeline_ETL
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Execute the ETL Process

1. **Extract Data:**
```bash
python scripts/extract.py
```

2. **Transform Data:**
```bash
python scripts/transform.py
```

3. **Load Data:**
```bash
python scripts/load.py
```

---

## 🌐 APIs Used

- **Rockets Data:** [`https://api.spacexdata.com/v4/rockets`](https://api.spacexdata.com/v4/rockets)
- **Launches Data:** [`https://api.spacexdata.com/v4/launches`](https://api.spacexdata.com/v4/launches)

---

## 📌 Notes

- Data is stored in **JSON** format across the Bronze, Silver, and Gold layers.
- Ensure the `delta_lake_data` directory exists before running the scripts.

---






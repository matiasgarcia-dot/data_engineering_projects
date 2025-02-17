# ETL Project: Argentina Risk Analysis

## Argentina Country Risk ETL (1995-2025)

This project implements an ETL (Extraction, Transformation, and Loading) process to analyze the evolution of Argentina's Country Risk from 1995 to 2025. The data is obtained from a public ( API https://argentinadatos.com/ ) and processed to facilitate analysis and visualization.

## Technologies Used

- Python 3.x
- Pandas
- Requests
- Power BI

## Project Structure

```
country_risk_ETL/
├── data/
│   └── transformed_data.csv
│
├── graphic_analysis/
│   ├── Country Risk Analysis of Argentina (1995 - 2025).pbit
│   └── Country Risk Analysis of Argentina (1995 - 2025).pdf
│
├── scripts/
│   ├── extract.py
│   └── transform.py
│
├── requirement.md
│
└── README.md
```

## Project Description

The goal of this project is to track and analyze Argentina's Country Risk index over three decades. This dataset allows us to observe trends, fluctuations, and critical points in the country's economic stability.

### ETL Process

1. **Extraction:**
   - Data is fetched from a public API providing Argentina's Country Risk index.

2. **Transformation:**
   - Rename and clean columns for better understanding.
   - Calculate the daily variation and percentage change.
   - Identify trends (Increase, Decrease, No Change).
   - Save the transformed data to a CSV file for visualization.

3. **Loading:**
   - Data is exported to Power BI for advanced visualization and analysis.

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/matiasgarcia-dot/data_engineering_projects.git
    cd data_engineering_projects/country_risk_ETL
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirement.md
    ```

4. Run the extraction and transformation scripts:

    ```bash
    python scripts/extract.py
    python scripts/transform.py
    ```

## Data Visualization

The project includes a Power BI report template (.pbit) and a PDF version with pre-generated visualizations:

- **Power BI Template:**
  - Interactive dashboard displaying Argentina's Country Risk trends.
  - Customizable for further analysis.

- **PDF Report:**
  - Static summary of key insights and trends from 1995 to 2025.





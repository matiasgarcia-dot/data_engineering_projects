
```md
# SpaceX ETL Process
This project performs an **ETL (Extract, Transform, Load)** process using SpaceX data.
The data is extracted from public APIs, transformed, and stored in different layers: Bronze, Silver, and Gold.

---

## Project Structure
spacex_data_pipeline_ETL/
│
└── delta_lake_data/
│    ├── bronze/
│    ├── silver/
│    └── gold/
│
└── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── README.md/
│
└── requirement.txt/

### Requirements
- Python 3.x  
- Visual Studio Code (VSCode)   

### Steps

1. **Install dependencies:**  
   In the terminal, run:
   ```bash
   pip install -r requirement.txt
   ```


2. **Run the scripts in order:**  
   
   - Extract data:
     ```bash
     python extract.py
     ```  
   - Transform data:
     ```bash
     python transform.py
     ```  
   - Load data:
     ```bash
     python load.py
     ```


---
## APIs Used
- Rockets: `https://api.spacexdata.com/v4/rockets`  
- Launches: `https://api.spacexdata.com/v4/launches`

---

## Notes
- JSON files are used for data storage in each layer.  




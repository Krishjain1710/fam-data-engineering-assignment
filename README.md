📊 Data Engineering Intern Assignment — Fam

This project transforms **daily stock price data** into **monthly aggregated datasets** while computing key **technical indicators** used in financial analysis.

The pipeline ingests 2 years of daily OHLC data for 10 stock tickers, performs monthly aggregation, calculates **SMA and EMA indicators**, and outputs **one CSV per ticker**.

The solution is implemented using **Python and Pandas only**, following a **modular, ETL-style design**.

🧱 Project Structure

fam-data-engineering-assignment/
│
├── data/
│   └── stocks_daily.csv
│
├── src/
│   ├── ingest.py
│   ├── transform.py
│   ├── indicators.py
│   ├── writer.py
│   └── main.py
│
├── output/
│   └── result_<TICKER>.csv
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
└── README.md

🔁 Pipeline Flow

1. **Ingestion**

   * Load CSV
   * Enforce schema & data types
   * Sort by ticker and date
   * Validate expected tickers

2. **Monthly Aggregation**

   * Convert daily data → monthly frequency
   * Apply OHLC rules:

     * Open → first trading day
     * Close → last trading day
     * High → monthly maximum
     * Low → monthly minimum

3. **Technical Indicators**

   * Calculated on **monthly close prices**
   * Simple Moving Average (SMA 10, SMA 20)
   * Exponential Moving Average (EMA 10, EMA 20)

4. **Partitioning**

   * One output CSV per ticker
   * Exactly 24 rows per file

---

## 📐 Technical Assumptions

* The dataset contains **only valid trading days**
* Each ticker has **complete data for all 24 months**
* No forward-filling or backfilling is applied
* SMA warm-up periods produce `NaN` values (expected behavior)
* EMA is initialized using Pandas’ exponential weighting (aligned with standard financial definitions)

---

## 📈 Indicator Formulas

### Simple Moving Average (SMA)

[
SMA_N = \frac{1}{N} \sum_{i=1}^{N} Close_i
]

### Exponential Moving Average (EMA)

[
EMA_t = (Price_t - EMA_{t-1}) \times \alpha + EMA_{t-1}
]

Where:

[
\alpha = \frac{2}{N + 1}
]

---

## ▶️ How to Run

```bash
pip install pandas
python src/main.py
```

After execution:

* The `output/` directory will contain **10 CSV files**
* Each file contains **24 monthly rows**

---

## ✅ Validation & Testing

Basic pipeline validations are included to ensure:

* Correct number of output files
* Correct row counts
* Correct ticker isolation
* Expected NaN behavior in SMA warm-up periods

---

## 🧠 Design Considerations

* Modular ETL-style code structure
* Vectorized Pandas operations only
* No external technical analysis libraries
* Clear separation of ingestion, transformation, and output logic

---

## 🚀 Future Improvements

* Add schema validation using Pandera
* Add unit tests for indicator math
* Store outputs in Parquet format

* Integrate with a data warehouse (BigQuery / Redshift)

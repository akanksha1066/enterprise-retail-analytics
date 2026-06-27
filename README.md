#  Enterprise Retail Analytics Platform

##  Project Overview

This repository contains a robust, end-to-end Data Engineering and Analytics platform that simulates enterprise retail transactions, processes data through an optimized ETL pipeline using Pandas, and visualizes executive insights via an interactive Streamlit dashboard.

---

##  Dashboard Preview

Here is how the live executive dashboard looks with interactive charts and real-time business KPIs:

![Dashboard Metrics](Screenshot%202026-06-27%20141139.png)
![Dashboard Data Table](Screenshot%202026-06-27%20141247.png)

---

##  Key Features

* **Data Simulation & Ingestion:** Simulates 6+ months of realistic retail transaction logs including sales metrics, customer profiles, product categories, and geographical distribution.
* **Optimized ETL Pipeline (`src/etl_pipeline.py`):** 
  * **Extraction:** Ingests raw multi-million row transactional datasets.
  * **Transformation:** Handles missing values, enforces proper schema datatypes, creates advanced computed metrics (e.g., Total Revenue), and performs high-performance aggregations.
  * **Loading:** Stores processed analytical datasets cleanly into specialized target directories.
* **Executive Dashboard (`src/app.py`):** Built using **Streamlit** and **Plotly** to serve interactive charts, dynamic Key Performance Indicators (KPIs), and detailed data previews for corporate stakeholders.

---

##  Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization & Frontend:** Streamlit, Plotly Express
* **Environment Management:** Python virtual environments (`requirements.txt`)

---

##  Project Structure

```text
enterprise-retail-analytics/
│
├── data/
│   ├── raw/                # Ingested raw datasets (transactions.csv)
│   └── processed/          # Aggregated results (category/city summaries)
│
├── src/
│   ├── etl_pipeline.py     # Backend Data Transformation logic
│   └── app.py              # Streamlit Dashboard application
│
└── requirements.txt        # System dependencies

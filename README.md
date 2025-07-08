# NYC Taxi Data Pipeline 🚖

A complete end-to-end Data Engineering project that ingests, processes, and visualizes NYC Yellow Taxi trip data using Docker, PostgreSQL, Apache Airflow, and Metabase.

## 🚀 Tech Stack

- **Apache Airflow** – Workflow orchestration
- **PostgreSQL** – Data warehouse
- **pgAdmin** – Database UI
- **Metabase** – Data visualization
- **Docker & Docker Compose** – Containerization

## 🧱 Architecture Overview

1. Data ingestion via Airflow into PostgreSQL.
2. Raw CSV loaded in chunks to avoid memory overflow.
3. Dashboards created in Metabase to analyze trip trends, revenues, and more.

## 📊 Visualizations

- Daily average fare
- Revenue per Month
- Average Trip Distance
- Tips per Month
- Top 10 pickup locations

## 📂 Project Structure

## bash
nyc_tax_data_pipeline/
│
├── dags/                  # Airflow DAGs and ETL logic
│   ├── ingest_data.py
│   └── ingest_yellow_taxi.py
│
├── docker-compose.yml     # Orchestrates the services
├── .gitignore             # Prevents large files and env data from being committed
├── README.md
//

## How to Run
## Start services
docker-compose up -d

## Access Airflow
http://localhost:8081

## Access pgAdmin
http://localhost:8080

## Access Metabase
http://localhost:3000


---

###  Push Everything

After finalizing your README and project files:

```bash
git add .
git commit -m "🧱 Finalize NYC Taxi pipeline with README and structure"
git push


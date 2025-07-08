etl:
	python etl/ingest_data.py

airflow:
	docker-compose up airflow

test:
	dbt test

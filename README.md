# Weather Data Pipeline
This project demonstrates a modern data pipeline built on a local environment, focusing on the Extract, Load, and Transform (ELT) process. The pipeline fetches weather data from an external API, loads it into a PostgreSQL database, and then uses dbt (data build tool) to perform data transformations. The entire workflow is orchestrated and automated with Apache Airflow.

## Project Overview
The primary goal of this pipeline is to ingest raw data and transform it into a clean, queryable format for analytics. This process is broken down into three main steps:

### Extract & Load: A Python script fetches raw weather data from a mock API and loads it into a staging table in the PostgreSQL database.

### Transform: dbt models are executed to clean, normalize, and enrich the raw data, creating a final, business-ready table.

### Orchestrate: Apache Airflow schedules and manages the execution of the ingestion and transformation tasks, ensuring the pipeline runs reliably.

This project is designed to be a fully self-contained, local setup, ideal for learning or development purposes without relying on cloud infrastructure.

## Tech Stack
This project leverages the following open-source technologies:

Python: The core programming language used for scripting and orchestration.

PostgreSQL: A powerful open-source relational database that serves as the data warehouse for both raw and transformed data.

dbt (data build tool): A command-line tool that enables data teams to transform data in their warehouse by writing modular SQL. It handles dependency management, testing, and documentation.

Apache Airflow: A platform for programmatically authoring, scheduling, and monitoring data workflows as Directed Acyclic Graphs (DAGs).

Git: Used for version control of the entire project.

Getting Started
Follow these steps to get the project up and running on your local machine.

Prerequisites
Windows Subsystem for Linux (WSL): This project is designed to run in a Linux environment. On Windows, please use WSL to ensure compatibility with Airflow.

Python 3.8+: The Python programming language and its package manager, pip, must be installed.

PostgreSQL: A running PostgreSQL instance with a database for this project (e.g., weather_data).

Local Setup
Clone the repository:

git clone <your_repo_url>
cd dbt_pipeline_project

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install "apache-airflow[postgres]" dbt-postgres psycopg2-binary

Configure dbt:

Create a profiles.yml file in your home directory (~/.dbt/).

Configure the connection to your PostgreSQL database.

dbt_project:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      port: 5432
      user: postgres
      password: <your_password>
      dbname: weather_data
      schema: analytics
      threads: 1

Initialize Airflow:

export AIRFLOW_HOME=$(pwd)
airflow db init
airflow users create --username admin --firstname John --lastname Doe --role Admin --email admin@example.com

Running the Pipeline
Once the setup is complete, you can run the pipeline.

Start Airflow services: Open two separate terminals.

Terminal 1 (Webserver): airflow webserver --port 8080

Terminal 2 (Scheduler): airflow scheduler

Access the Airflow UI: Navigate to http://localhost:8080 in your browser.

Trigger the DAG: Find the weather_data_pipeline DAG and manually trigger a run.

The pipeline will first run the ingestion script and then the dbt models, and you will see the results reflected in your PostgreSQL database.

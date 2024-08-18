# austin-bikeshare-trips-etl-airflow
Create an ETL pipeline using Apache Airflow to manage the end-to-end data flow. The goal is to extract Bikeshare data from a public dataset (austin_bikeshare) in BigQuery, transform and store the data in Google Cloud Storage (GCS) in a partitioned format, and then create an external table in BigQuery to facilitate querying and analysis

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: Install [Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Install [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

```
austin-biketrips-etl
├── dags/
│   ├── bikeshare_etl.py
│   ├── bikeshare_etl.yaml
│   └── service_account.json
├── logs/
├── plugins/
├── Dockerfile
└── docker-compose.yaml

- dags/: Contains the DAG scripts, the YAML configuration file, and the Google Cloud service account JSON file.
- logs/: Directory for Airflow logs.
- plugins/: Directory for Airflow plugins.
- Dockerfile/: Defines the Docker image for the Airflow environment.
- docker-compose.yaml: Docker Compose file to set up Airflow services.

- You can replace austin-biketrips-etl with the working directory of docker.
```

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

### Step 2: Configure Google Cloud Credentials

Place your Google Cloud service account JSON file in the `dags/` directory and name it `service_account.json`.
the service account should have the following roles: BigQuery Admin,  Storage Admin, and Viewer

### Step 3: Build the Docker Image

Build the Docker image using the provided `Dockerfile`:

```sh
docker-compose build
```

### Step 4: Initialize the Airflow Database

Initialize the Airflow database:

```sh
docker-compose run airflow-init
```

### Step 5: Start Airflow Services

Start the Airflow web server and scheduler:

```sh
docker-compose up -d
```

### Step 6: Access the Airflow Web UI

Open your browser and go to [http://localhost:8080](http://localhost:8080) to access the Airflow web interface.

### Step 6: DAG verification
- DAG Graph
  <img width="932" alt="image" src="https://github.com/user-attachments/assets/61d6fb4c-e861-45b2-acab-701780739157">

 - Parquet files in GCS bucket
 <img width="863" alt="image" src="https://github.com/user-attachments/assets/81024f68-4a0b-4cf2-a353-46a2d771df84">

 - External BigLake Table
 
 <img width="804" alt="image" src="https://github.com/user-attachments/assets/b526e879-490d-46f5-9c35-4ed737ab96da">



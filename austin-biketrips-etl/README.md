Here's a `README.md` file based on the content you provided:

```markdown
# Bikeshare ETL Project

This project sets up an Apache Airflow environment to perform ETL (Extract, Transform, Load) operations on bikeshare data. The data is read from Google Cloud Storage and loaded into a BigQuery table.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: Install [Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Install [Docker Compose](https://docs.docker.com/compose/install/)
- **Google Cloud SDK**: Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

## Project Structure

```
airflow-docker/
├── dags/
│   ├── bikeshare_etl.py
│   ├── bikeshare_etl.yaml
│   └── service_account.json
├── logs/
├── plugins/
├── Dockerfile
└── docker-compose.yml
```

- **dags/**: Contains the DAG scripts, the YAML configuration file, and the Google Cloud service account JSON file.
- **logs/**: Directory for Airflow logs.
- **plugins/**: Directory for Airflow plugins.
- **Dockerfile**: Defines the Docker image for the Airflow environment.
- **docker-compose.yml**: Docker Compose file to set up Airflow services.

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```sh
git clone <repository-url>
cd airflow-docker
```

### Step 2: Configure Google Cloud Credentials

Place your Google Cloud service account JSON file in the `dags/` directory and name it `service_account.json`.

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
```

You can copy this content into a `README.md` file in your project repository. Let me know if you need any adjustments!
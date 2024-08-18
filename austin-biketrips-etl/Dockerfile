# Use the official Airflow image
FROM apache/airflow:2.10.0

# Switch to root user to install additional packages
USER root

# Install Google Cloud SDK
RUN apt-get update && apt-get install -y gnupg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get install -y apt-transport-https ca-certificates && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update && apt-get install -y google-cloud-sdk

# Switch back to airflow user
USER airflow

# Copy DAGs and other necessary files
COPY dags/ /opt/airflow/dags/
COPY dags/service_account.json /opt/airflow/dags/service_account.json

# Set environment variables for Google Cloud authentication
ENV GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/dags/service_account.json


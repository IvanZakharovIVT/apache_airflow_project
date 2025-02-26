FROM apache/airflow:2.6.3-python3.11

# Install additional requirements BEFORE switching to airflow user
RUN pip install --no-cache-dir uv

# Switch to airflow user
USER airflow

# Copy and install remaining requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /home/airflow
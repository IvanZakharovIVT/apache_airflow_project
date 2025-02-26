FROM apache/airflow:2.6.0-python3.9
USER root
COPY requirements.txt ./requirements.txt
USER airflow
RUN pip install uv && \
    uv pip install -r requirements.txt --system && \
    pip uninstall -y uv && \
    apk del build-deps && \
    rm -rf /var/cache/apk/*
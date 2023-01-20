FROM python:3.9

WORKDIR /elasticsearch-with-docker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY elasticsearch_index_creation.py .

CMD ["python", "elasticsearch_index_creation.py"]

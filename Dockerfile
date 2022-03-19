FROM python:3.9-slim

COPY requirements.txt /src/requirements.txt
WORKDIR /src

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    && python -m pip install --no-cache-dir -r ./requirements.txt \
    && python -m pip install --no-cache-dir gunicorn \
    && rm -rf /var/lib/apt/lists/*

COPY . .

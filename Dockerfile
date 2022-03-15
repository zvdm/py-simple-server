FROM python:3.9-slim

COPY . /src
WORKDIR /src

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    && pip install -r ./requirements.txt \
    && rm -rf /var/lib/apt/lists/*
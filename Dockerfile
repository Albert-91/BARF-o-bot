# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

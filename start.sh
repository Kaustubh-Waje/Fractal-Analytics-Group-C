#!/bin/bash

echo "Starting Docker containers..."
docker compose up -d

echo "Waiting for PostgreSQL..."
until docker exec postgres pg_isready -U kaustubh >/dev/null 2>&1
do
    sleep 2
done
echo "PostgreSQL is ready."

echo "Waiting for Kafka..."
sleep 10

echo "Creating Kafka topic if it doesn't exist..."
docker exec kafka kafka-topics \
    --bootstrap-server localhost:9092 \
    --create \
    --if-not-exists \
    --topic invoice-topic \
    --partitions 1 \
    --replication-factor 1

echo "Project is ready!"
echo ""
echo "Open API docs:"
echo "http://localhost:8000/docs"

#!/bin/bash

echo "========== Containers =========="
docker ps

echo ""
echo "========== Kafka Topics =========="
docker exec kafka kafka-topics \
--bootstrap-server localhost:9092 \
--list

echo ""
echo "========== PostgreSQL =========="
docker exec postgres psql -U kaustubh -d procurement \
-c "SELECT COUNT(*) FROM kafka_invoices;"

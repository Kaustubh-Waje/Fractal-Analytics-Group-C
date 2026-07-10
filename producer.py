from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

invoice = {
    "vendor": "Kaustubh",
    "amount": 15000,
    "status": "Pending"
}

producer.send("invoice-topic", invoice)
producer.flush()


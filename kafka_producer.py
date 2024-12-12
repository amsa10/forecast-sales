from confluent_kafka import Producer
import json
import random
import time

# Kafka configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})  # Update with your Kafka broker

topic = 'sales_data'  # Kafka topic

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Simulate sales data and send to Kafka
for i in range(1000):  # Simulating 1000 messages
    data = {
        "customer_id": f"customer_{i}",
        "transaction_amount": random.uniform(10.0, 500.0),
        "transaction_date": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    producer.produce(topic, key=str(i), value=json.dumps(data), callback=delivery_report)
    producer.flush()
    time.sleep(0.1)  # Simulate time between transactions

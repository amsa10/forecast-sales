from confluent_kafka import Producer
import random
import time
import json

# Set up the Kafka producer
producer = Producer({'bootstrap.servers': 'kafka:9093'})

# Define Kafka topic
topic = 'sales_data'

def generate_sales_data():
    """Generate random sales data."""
    customer_id = random.randint(1000, 9999)
    transaction_amount = round(random.uniform(10, 500), 2)
    transaction_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    return {'customer_id': customer_id, 'transaction_amount': transaction_amount, 'transaction_date': transaction_date}

def on_delivery(err, msg):
    """Callback function to check message delivery."""
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Send data every 1 second
while True:
    sales_data = generate_sales_data()
    producer.produce(topic, json.dumps(sales_data), callback=on_delivery)
    producer.flush()
    time.sleep(1)

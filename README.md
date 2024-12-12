# forecast-sales


![image](https://github.com/user-attachments/assets/c5a0a28d-ac48-4f89-91fd-149b8c6a9668)


# Sales Forecasting Project

This project demonstrates how to use **Kafka**, **Faust**, **TensorFlow Serving**, and **Docker** to build a real-time sales forecasting pipeline.

## Components

1. **Kafka Producer**: Simulates the real-time streaming of sales data.
2. **Faust Consumer**: Consumes the data from Kafka, sends it to TensorFlow Serving for predictions.
3. **TensorFlow Serving**: Serves the trained model and handles predictions.

## Setup

1. Build Docker images:
   ```bash
   docker-compose build


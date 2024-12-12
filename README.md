# forecast-sales

![image](https://github.com/user-attachments/assets/e2c7cb23-8b4d-42cf-b922-1d0886d08e0a)



# Sales Forecasting Project

This project implements a real-time sales forecasting system using Kafka, TensorFlow Serving, Faust, and Docker. It allows for the continuous stream of sales data, real-time prediction, and deployment in the cloud.

## Components

1. **Kafka Producer**: Simulates the real-time streaming of sales data.
2. **Faust Consumer**: Consumes the data from Kafka, sends it to TensorFlow Serving for predictions.
3. **TensorFlow Serving**: Serves the trained model and handles predictions.

## Setup

1. Build Docker images:
   ```bash
   docker-compose build


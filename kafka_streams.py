import faust
import requests
import json

# Set up Faust app to connect to Kafka
app = faust.App('sales-forecast-app', broker='kafka://localhost:9092')  # Update with your Kafka broker
sales_topic = app.topic('sales_data', value_type=dict)

@app.agent(sales_topic)
async def process_sales_data(stream):
    async for sale in stream:
        # Example: Extract features (just the transaction amount here)
        features = [sale['transaction_amount']]

        # Send the data to TensorFlow Serving for prediction
        response = requests.post(
            'http://localhost:8501/v1/models/sales_model:predict',  # TensorFlow Serving endpoint
            json={'instances': [{'features': features}]}
        )
        prediction = response.json()
        print(f"Predicted sales for {sale['customer_id']}: {prediction['predictions']}")

if __name__ == '__main__':
    app.main()

import faust
import requests
import json

# Set up Faust app to connect to Kafka
app = faust.App('sales-forecast-app', broker='kafka://localhost:9093')  # Use Kafka broker
sales_topic = app.topic('sales_data', value_type=dict)

@app.agent(sales_topic)
async def process_sales_data(stream):
    async for sale in stream:
        # Extract the transaction amount from the sale data
        features = [sale['transaction_amount']]

        # Send the features to TensorFlow Serving for prediction
        response = requests.post(
            'http://tensorflow-serving:8501/v1/models/sales_model:predict',  # TensorFlow Serving endpoint
            json={'instances': [{'features': features}]}
        )
        
        if response.status_code == 200:
            prediction = response.json()
            print(f"Predicted sales for {sale['customer_id']}: {prediction['predictions']}")
        else:
            print(f"Error with prediction: {response.text}")

if __name__ == '__main__':
    app.main()


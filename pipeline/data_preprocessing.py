import tensorflow as tf
import numpy as np
from pipeline.database import get_connection

def fetch_sales_data(batch_size: int = 32):
    """Fetch data from the cloud database in batches."""
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT customer_id, transaction_amount, transaction_date FROM sales"
    cursor.execute(query)

    while True:
        batch_data = []
        for _ in range(batch_size):
            row = cursor.fetchone()
            if row is None:
                break
            batch_data.append(row)

        if not batch_data:
            break

        yield batch_data

    conn.close()

def preprocess_data(batch_data):
    """Convert the raw batch of data into a TensorFlow dataset."""
    # Extract features (transaction_amounts) and labels (e.g., customer_id)
    transaction_amounts = np.array([row[1] for row in batch_data], dtype=np.float32)
    customer_ids = np.array([row[0] for row in batch_data], dtype=np.int32)  # Example: Customer ID

    # Return a tuple of (features, labels) for the dataset
    features = tf.convert_to_tensor(transaction_amounts)
    labels = tf.convert_to_tensor(customer_ids)  # Example: This could be adjusted based on the task
    
    return features, labels

def create_tf_dataset(batch_size: int = 32):
    """Creates a TensorFlow Dataset from the fetch_sales_data function."""
    dataset = tf.data.Dataset.from_generator(
        lambda: fetch_sales_data(batch_size),  # Generator function for fetching data
        output_signature=(
            tf.TensorSpec(shape=(batch_size,), dtype=tf.float32),  # Shape of transaction_amounts
            tf.TensorSpec(shape=(batch_size,), dtype=tf.int32)     # Shape of customer_ids (or other labels)
        )
    )
    # Process the data
    dataset = dataset.map(lambda batch_data: preprocess_data(batch_data))

    return dataset

# Example of creating a dataset and inspecting the first few items
if __name__ == "__main__":
    dataset = create_tf_dataset(batch_size=32)
    
    # Iterate over the dataset and inspect the output
    for features, labels in dataset.take(1):  # Take 1 batch for inspection
        print(f"Features (Transaction Amounts): {features.numpy()}")
        print(f"Labels (Customer IDs): {labels.numpy()}")

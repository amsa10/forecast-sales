import tensorflow as tf
import numpy as np

def preprocess_data(batch_data):
    """Preprocess the sales data and return TensorFlow dataset."""
    transaction_amounts = np.array([row[1] for row in batch_data], dtype=np.float32)
    
    # Here, we do not normalize as per the previous request.
    dataset = tf.data.Dataset.from_tensor_slices(transaction_amounts)
    dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE).cache()
    
    return dataset

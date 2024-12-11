import tensorflow as tf
from pipeline.data_preprocessing import fetch_sales_data, preprocess_data
from pipeline.model import create_model

def train_model():
    """Train the model using data from the cloud database."""
    model = create_model()

    # Setup the data pipeline using TensorFlow Dataset
    batch_size = 32
    dataset = tf.data.Dataset.from_generator(
        lambda: fetch_sales_data(batch_size),
        output_signature=tf.TensorSpec(shape=(batch_size, 1), dtype=tf.float32)
    )

    dataset = dataset.map(lambda batch: preprocess_data(batch))

    # Set up model checkpoint callback
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        'model_checkpoint.h5', save_best_only=True
    )

    # Train the model
    model.fit(dataset, epochs=10, callbacks=[checkpoint_callback])

    # Save the final model
    model.save('sales_model.h5')

if __name__ == "__main__":
    train_model()

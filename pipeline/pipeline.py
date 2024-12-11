import tensorflow as tf
from pipeline.data_preprocessing import fetch_sales_data, preprocess_data
from pipeline.model import create_model
import tensorflow as tf
import mlflow
import mlflow.keras
from pipeline.database import get_connection

def train_model(batch_size: int = 32, epochs: int = 10):
    """Train the model and track experiments with MLflow."""
    with mlflow.start_run():
        mlflow.log_param("batch_size", batch_size)
        mlflow.log_param("epochs", epochs)
        
        model = create_model()
        dataset = create_tf_dataset(batch_size=batch_size)

        # Train the model
        model.fit(dataset, epochs=epochs)

        # Log metrics to MLflow
        for epoch in range(epochs):
            loss = model.history.history['loss'][epoch]
            mae = model.history.history['mae'][epoch]
            mlflow.log_metric("loss", loss, step=epoch)
            mlflow.log_metric("mae", mae, step=epoch)

        # Log the trained model with MLflow
        mlflow.keras.log_model(model, "sales_model")

if __name__ == "__main__":
    train_model(batch_size=32, epochs=10)

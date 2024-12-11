import mlflow
import mlflow.keras

def log_model(model, model_name):
    mlflow.keras.log_model(model, model_name)
    print(f"Model {model_name} logged to MLflow.")

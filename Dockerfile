# Use the official TensorFlow Serving image
FROM tensorflow/serving:latest

# Copy the saved model to the container
COPY ./models /models

# Expose the default port used by TensorFlow Serving
EXPOSE 8501

# Command to start TensorFlow Serving
CMD ["tensorflow_model_server", "--model_name=sales_model", "--model_base_path=/models/sales_model"]

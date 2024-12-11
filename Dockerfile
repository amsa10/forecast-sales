# Use an official TensorFlow image as the base image
FROM tensorflow:2.11.0

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose port for MLflow tracking server (optional)
EXPOSE 5000

# Set the default command to run the sales data pipeline
CMD ["python", "pipeline/sales_data_pipeline.py"]


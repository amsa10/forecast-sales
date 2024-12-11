# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional, can be overwritten by Docker Compose or -e flag)
ENV DB_TYPE mysql

# Expose any necessary ports (optional, if needed)
EXPOSE 5000  # If running a web server, not necessary for this case

# Run the application
CMD ["python", "pipeline/pipeline.py"]

# forecast-sales


![image](https://github.com/user-attachments/assets/c5a0a28d-ac48-4f89-91fd-149b8c6a9668)


docker build -t sales-pipeline .

docker-compose up --build

docker-compose down

After running the Docker container or Docker Compose, the sales data pipeline will execute:

It will connect to the cloud database.
It will fetch the data in batches.
The data will be preprocessed and fed into the model.
The model will train and save checkpoints, and finally, the trained model will be saved as sales_model.h5.

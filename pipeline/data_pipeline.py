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


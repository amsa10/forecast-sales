import mysql.connector
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_mysql_connection():
    """Connect to a cloud MySQL database."""
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=3306,
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return connection

def get_postgres_connection():
    """Connect to a cloud PostgreSQL database."""
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=5432,
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return connection

def get_connection():
    """Return a connection based on the DB_TYPE."""
    db_type = os.getenv('DB_TYPE', 'mysql').lower()
    if db_type == 'mysql':
        return get_mysql_connection()
    elif db_type == 'postgres':
        return get_postgres_connection()
    else:
        raise ValueError("DB_TYPE must be 'mysql' or 'postgres'.")

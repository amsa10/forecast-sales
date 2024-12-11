import psycopg2

def get_connection():
    """Connect to your cloud database (PostgreSQL in this case)."""
    conn = psycopg2.connect(
        host="your-db-host",
        database="your-db-name",
        user="your-db-user",
        password="your-db-password"
    )
    return conn


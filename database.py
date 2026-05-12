import psycopg2
import os

def get_db_connection():
    database_url = os.environ.get("DATABASE_URL")

    if database_url:
        # Render provides the URL directly
        conn = psycopg2.connect(database_url)
    else:
        # Local development fallback
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="genz_app",
            user="postgres",
            password=os.environ.get("DB_PASSWORD", "Honey9949"),
            port="5433"
        )
    return conn

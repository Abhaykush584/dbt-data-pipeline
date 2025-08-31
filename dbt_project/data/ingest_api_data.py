import requests
import psycopg2
import os

# Database connection details from your dbt profile
DB_HOST = "localhost"
DB_NAME = "weather_data"
DB_USER = "postgres"
DB_PASSWORD = "akks1925@"
DB_PORT = 5432

API_URL = "https://your-weather-api-url.com/data"

def ingest_data():
    """
    Fetches data from an API and loads it into a PostgreSQL staging table.
    """
    conn = None
    try:
        # Fetch data from the API
        response = requests.get(API_URL)
        response.raise_for_status() # Raise an error for bad status codes
        data = response.json()

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()

        # Create a staging table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS analytics.stg_weather_data (
                -- Define your columns here
                timestamp_utc TIMESTAMP,
                temperature FLOAT,
                humidity FLOAT,
                -- etc...
            );
        """)

        # Truncate the table to get fresh data
        cur.execute("TRUNCATE TABLE analytics.stg_weather_data;")

        # Insert the data
        for record in data:
            # You'll need to adjust this to match your API's data structure
            cur.execute("""
                INSERT INTO analytics.stg_weather_data (timestamp_utc, temperature, humidity)
                VALUES (%s, %s, %s);
            """, (record['timestamp'], record['temp'], record['hum']))

        conn.commit()
        print("Data loaded successfully!")

    except (psycopg2.Error, requests.RequestException) as e:
        print(f"Error occurred: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    ingest_data()
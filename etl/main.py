import psycopg2
import pandas as pd

def extract():
    # Подключение к PostgreSQL
    conn = psycopg2.connect(
        dbname="etl_db", user="etl_user", password="etl_pass", host="postgres", port="5432"
    )
    query = "SELECT * FROM raw_data"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

def load(data):
    conn = psycopg2.connect(
        dbname="etl_db", user="etl_user", password="etl_pass", host="postgres", port="5432"
    )
    data.to_sql('staging_data', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    data = extract()
    load(data)

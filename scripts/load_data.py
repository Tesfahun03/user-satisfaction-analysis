import psycopg2
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv


load_dotenv()


DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
print(DB_USER,DB_NAME)


def load_postgres_data(query):

    try:
        connection = psycopg2.connect(
            host = DB_HOST,
            port = DB_PORT,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD
        )
    except Exception as e:
        print(f'Failed trying to connect with DB: {e}')
        return None

    if connection:
        try:
            df = pd.read_sql_query(query, connection)

            connection.close()
            return df
        
        except Exception as e:
            print('unable to fetch the data:  {e}')
            return None



import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv(".env")

host: str = os.getenv("HOST")
database: str = os.getenv("DATABASE")
user: str = os.getenv("USER")
password: str = os.getenv("PASSWORD")


def connect_to_database():
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
    )
    return conn

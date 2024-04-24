import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(".env")

# host: str = os.getenv("HOST")
# database: str = os.getenv("DATABASE")
# user: str = os.getenv("USER")
# password: str = os.getenv("PASSWORD")


# def connect_to_db():
#     conn = psycopg2.connect(
#         host=host,
#         database=database,
#         user=user,
#         password=password,
#     )
#     return conn


# db_connection = connect_to_db()

# neon.tech psql
pguser: str = os.getenv("PGUSER")
pghost: str = os.getenv("PGHOST")
pgdatabase: str = os.getenv("PGDATABASE")
pgpassword: str = os.getenv("PGPASSWORD")
# pgport: str = os.getenv("PGPORT")


def connect_to_db():
    conn = psycopg2.connect(
        user=pguser,
        host=pghost,
        database=pgdatabase,
        password=pgpassword,
        # port=pgport,
    )
    return conn


db_connection = connect_to_db()

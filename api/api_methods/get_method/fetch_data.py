from psycopg2.extras import RealDictCursor
from database.database import db_connection


def fetch_latest_data(db_connection):
    conn = db_connection
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = """SELECT * FROM jobs ORDER BY scrape_time DESC LIMIT 25;"""
        cursor.execute(query)
        data = cursor.fetchall()

        return data


dataframe = fetch_latest_data(db_connection)

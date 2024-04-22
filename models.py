from database import db_connection
from psycopg2.extras import RealDictCursor


def create_jobs_table():
    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
      id SERIAL PRIMARY KEY,
      title_text VARCHAR(50),
      title_href VARCHAR(255),
      company_text VARCHAR(50),
      company_href VARCHAR(255),
      scrape_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()


create_jobs_table()

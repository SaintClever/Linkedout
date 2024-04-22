from database.database import db_connection
from psycopg2.extras import RealDictCursor


def create_jobs_table():
    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
      id SERIAL PRIMARY KEY,
      job_title VARCHAR(255),
      job_href VARCHAR(255),
      company_title VARCHAR(255),
      company_href VARCHAR(255),
      scrape_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

    table_name = create_table_query.split()[5]
    print(table_name, "table successfully created")


create_jobs_table()

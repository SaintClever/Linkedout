from database.database import db_connection
from psycopg2.extras import RealDictCursor


def create_jobs_table():
    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
      id SERIAL PRIMARY KEY,
      company_name VARCHAR(200),
      job_title VARCHAR(200),
      job_href VARCHAR(200),
      location VARCHAR(200),
      currency VARCHAR(20),
      starting_salary INTEGER,
      max_salary INTEGER,
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

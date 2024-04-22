import os
from database.database import db_connection
from .scrape_himalayas import himalayas_jobs
from psycopg2.extras import RealDictCursor


def insert_job_data(db_connection, himalayas_jobs):
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(file_path)

    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = """
    INSERT INTO jobs (
      job_title,
      job_href,
      company_title,
      company_href
    ) VALUES (%s, %s, %s, %s)
    """

    for data in himalayas_jobs:
        cursor.execute(
            query,
            (
                data["job_title"],
                data["job_href"],
                data["company_title"],
                data["company_href"],
            ),
        )
    conn.commit()
    cursor.close()
    conn.close()

    print("Data inserted successfully from:", file_name)


insert_himalayas = insert_job_data(db_connection, himalayas_jobs)

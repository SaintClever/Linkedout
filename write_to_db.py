from database import db_connection
from himalayas import himalayas_jobs
from psycopg2.extras import RealDictCursor


def insert_job_data(db_connection, himalayas_jobs):
    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = """
    INSERT INTO jobs (
      title_text,
      title_href,
      company_text,
      company_href
    ) VALUES (%s, %s, %s, %s)
    """

    for data in himalayas_jobs:
        data["title_text"] = data["title_text"][:50]
        cursor.execute(
            query,
            (
                data["title_text"],
                data["title_href"],
                data["company_text"],
                data["company_href"],
            ),
        )
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully")


insert_job_data(db_connection, himalayas_jobs)

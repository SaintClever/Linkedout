import os
from psycopg2.extras import RealDictCursor


def insert_job_data(db_connection, user_jobs):
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(file_path)

    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = """
    INSERT INTO jobs (
        company_name,
        job_title,
        job_href,
        location,
        currency,
        starting_salary,
        max_salary
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            user_jobs["company_name"],
            user_jobs["job_title"],
            user_jobs["job_href"],
            user_jobs["location"],
            user_jobs["currency"],
            user_jobs["starting_salary"],
            user_jobs["max_salary"],
        ),
    )
    conn.commit()
    cursor.close()
    conn.close()

    print("Data inserted successfully from:", file_name)

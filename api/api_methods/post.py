import os
from psycopg2.extras import RealDictCursor


def post(db_connection, data):
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
            data["company_name"],
            data["job_title"],
            data["job_href"],
            data["location"],
            data["currency"],
            data["starting_salary"],
            data["max_salary"],
        ),
    )
    conn.commit()
    # cursor.close()
    # conn.close()

    print("Data inserted successfully from:", file_name)

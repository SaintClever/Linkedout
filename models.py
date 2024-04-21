import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
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

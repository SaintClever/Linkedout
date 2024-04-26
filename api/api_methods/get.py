import random
from database.database import db_connection
from data_analysis.matplotlib_visuals.colors import colors
from psycopg2.extras import RealDictCursor
import matplotlib.pyplot as plt

print(db_connection)


# NOTE: Incomplete
def request_latest_data(db_connection):
    conn = db_connection
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = """
    SELECT * FROM jobs"""
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


print(request_latest_data(db_connection))
# def create_salary_plot():
#     # fetch_latest_data is a hypothetical function
#     df = request_latest_data(db_connection)
#     fig, ax = plt.subplots()

#     ax.plot(
#         df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
#         df["max_salaries"],
#         label="Max Salaries",
#         color=random.choice(colors),
#         marker="o",
#         linestyle="-",
#     )

#     ax.plot(
#         df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
#         df["starting_salaries"],
#         label="Starting Salaries",
#         color=random.choice(colors),
#         marker="o",
#         linestyle="-",
#     )

#     return fig

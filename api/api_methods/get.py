import random
from database.database import db_connection
from data_analysis.matplotlib_visuals.colors import colors
from psycopg2.extras import RealDictCursor
import pandas as pd
import matplotlib.pyplot as plt


# NOTE: Incomplete
def fetch_latest_data(db_connection):
    # conn = db_connection
    # cursor = conn.cursor(cursor_factory=RealDictCursor)
    # query = """SELECT * FROM jobs;"""
    # cursor.execute(query)
    # data = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # return data

    conn = db_connection
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = """SELECT * FROM jobs;"""
        cursor.execute(query)
        data = cursor.fetchall()

    return data


def create_salary_plot():
    # fetch_latest_data is a hypothetical function
    dataframe = fetch_latest_data(db_connection)

    (
        company_names,
        job_titles,
        locations,
        currencies,
        starting_salaries,
        max_salaries,
    ) = [[] for _ in range(6)]

    for i, df in enumerate(dataframe):
        company_names.append(df["company_name"])
        job_titles.append(df["job_title"])
        locations.append(df["location"])
        currencies.append(df["currency"])
        starting_salaries.append(df["starting_salary"])
        max_salaries.append(df["max_salary"])

        # Request only 25 jobs be presented
        if i == 25:
            break

    data = {
        "company_names": company_names,
        "job_titles": job_titles,
        "locations": locations,
        "currencies": currencies,
        "starting_salaries": starting_salaries,
        "max_salaries": max_salaries,
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(15, 8))

    # Plot the data
    ax.barh(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
        df["max_salaries"],
        label="Max Salaries",
        color=random.choice(colors),
        height=0.4,  # Adjust the height of the bars
    )

    ax.barh(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
        df["starting_salaries"],
        label="Starting Salaries",
        color=random.choice(colors),
        height=0.4,  # Adjust the height of the bars
    )

    # Adjust x-axis tick labels
    ax.set_yticklabels(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
        # rotation=45,  # Rotate the labels by 45 degrees
        horizontalalignment="right",  # Align the labels to the right
        fontsize=10,  # Adjust the font size of the labels
    )

    # Add labels and legend
    ax.set_xlabel("Salaries")
    ax.set_ylabel("Companies - Jobs - Locations")
    ax.legend()

    # Show plot
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping

    return fig


create_salary_plot()

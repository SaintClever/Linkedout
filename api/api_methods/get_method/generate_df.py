# import random
from .fetch_data import dataframe
import pandas as pd


def generate(dataframe):
    (
        company_names,
        job_titles,
        locations,
        currencies,
        starting_salaries,
        max_salaries,
    ) = [[] for _ in range(6)]

    # Request only 25 jobs be presented
    for i, df in enumerate(dataframe):
        company_names.append(df["company_name"])
        job_titles.append(df["job_title"])
        locations.append(df["location"])
        currencies.append(df["currency"])
        starting_salaries.append(df["starting_salary"])
        max_salaries.append(df["max_salary"])
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

    return pd.DataFrame(data)


df = generate(dataframe)

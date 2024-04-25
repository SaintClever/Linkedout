from .data_manipulation import df
import pandas as pd

# Pre-cleaned data to CSV
df.to_csv("data_analysis/pandas_data/processed_job_data.csv", index=False)
df = pd.read_csv("data_analysis/pandas_data/processed_job_data.csv")

company_names, job_titles, locations, currencies, starting_salaries, max_salaries = [
    [] for i in range(6)
]
count = 0

while count != 25:  # controls the number of rows in charts displayed
    company_names.append(df["company_name"][count])
    job_titles.append(df["job_title"][count])
    locations.append(df["location"][count])
    currencies.append(df["currency"][count])
    starting_salaries.append(df["starting_salary"][count])
    max_salaries.append(df["max_salary"][count])
    count += 1

data = {
    "company_names": company_names,
    "job_titles": job_titles,
    "locations": locations,
    "currencies": currencies,
    "starting_salaries": starting_salaries,
    "max_salaries": max_salaries,
}

df = pd.DataFrame(data)
# print(df)

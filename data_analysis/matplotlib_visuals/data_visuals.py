import pandas as pd

df = pd.read_csv("data_analysis/pandas_data/processed_job_data.csv")
print(df)

colors = [
    "lightcoral",
    "maroon",
    "salmon",
    "chocolate",
    "peru",
    "bisque",
    "moccasin",
    "khaki",
    "chartreuse",
    "darkseagreen",
    "turquoise",
    "teal",
    "steelblue",
    "slategray",
    "royalblue",
    "slateblue",
    "indigo",
    "fuchsia",
    "orchid",
    "crimson",
]

company_names, job_titles, locations, currencies, starting_salaries, max_salaries = [
    [] for i in range(6)
]
count = 0

while count != 25:
    company_names.append(df["company_name"][count])
    job_titles.append(df["job_title"][count])
    locations.append(df["location"][count])
    currencies.append(df["currency"][count])
    starting_salaries.append(df["starting_salary"][count])
    max_salaries.append(df["max_salary"][count])
    count += 1

countries = {
    "AR": "Argentina",
    "CA": "Canada",
    "CZ": "Czech Republic",
    "DZ": "Algeria",
    "GB": "United Kingdom",
    "IE": "Ireland",
    "PH": "Philippines",
    "RO": "Romania",
    "TW": "Taiwan",
    "US": "United States",
}
country_names = [countries[i] for i in locations if i in countries.keys()]

data = {
    "company_names": company_names,
    "job_titles": job_titles,
    "locations": locations,
    "currencies": currencies,
    "starting_salaries": starting_salaries,
    "max_salaries": max_salaries,
    # "country_names": country_names, # ValueError: All arrays must be of the same length
}

df = pd.DataFrame(data)

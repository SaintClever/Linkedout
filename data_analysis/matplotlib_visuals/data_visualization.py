import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_analysis/pandas_data/processed_job_data.csv")
print(df)

company_names, job_titles, locations, currencies, starting_salaries, max_salaries = [
    [] for i in range(6)
]
count = 0

while count != 35:
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

# Plot Chart
df = pd.DataFrame(data)

plt.figure(figsize=(15, 8))
plt.plot(
    df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
    df["max_salaries"],
    color="teal",
    marker="o",
    linestyle="-",
)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Max Salaries Based on Country Code", fontsize=10)
plt.ylabel("Job Title", fontsize=10)
plt.title("Max Salaries for Different Job Titles", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig("data_analysis/matplotlib_visuals/plot.png", bbox_inches="tight")
plt.close()

# barh chart
df = pd.DataFrame(data)
df = df.sort_values(by="max_salaries", ascending=False)  # Sorting data by max_salaries

plt.figure(figsize=(15, 8))
plt.barh(
    df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
    df["max_salaries"],
    color="purple",
)
plt.xlabel("Max Salaries Based on Country Code", fontsize=10)
plt.ylabel("Job Title", fontsize=10)
plt.title("Max Salaries for Different Job Titles", fontsize=10)
plt.gca().invert_yaxis()  # Invert y-axis to have the highest salary at the top
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig("data_analysis/matplotlib_visuals/barh.png", bbox_inches="tight")
plt.close()

import random
from .colors import colors
from data_analysis.pandas_data.data_to_csv import df
import pandas as pd
import matplotlib.pyplot as plt

differ = [
    f"{max_salary - df["starting_salaries"][i]:,}"
    for i, max_salary in enumerate(df["max_salaries"])
]

difference = pd.DataFrame({"difference": differ})

# Line Plot
def line_plot(df):
    plt.figure(figsize=(15, 8))
    plt.plot(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["max_salaries"],
        label="Max Salaries",
        color=random.choice(colors),
        marker="o",
        linestyle="-",
    )
    plt.plot(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["starting_salaries"],
        label="Starting Salaries",
        color=random.choice(colors),
        marker="o",
        linestyle="-",
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Max Salaries Based on Country Code", fontsize=10)
    plt.ylabel("Companies - Jobs - Locations", fontsize=10)
    plt.title("Max Salaries for Different Job Titles", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.legend()
    plt.savefig(
        "data_analysis/matplotlib_visuals/images/line_plot.png", bbox_inches="tight"
    )
    plt.show()
    plt.close()


# Bar Plot
def bar_plot(df):
    plt.figure(figsize=(15, 8))
    plt.bar(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["max_salaries"],
        label="Max Salaries",
        color=random.choice(colors),
        linestyle="-",
    )
    plt.bar(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["starting_salaries"],
        label="Starting Salaries",
        color=random.choice(colors),
        linestyle="-",
    )
    plt.xticks(rotation=80)
    plt.xlabel("Max Salaries Based on Country Code", fontsize=10)
    plt.ylabel("Companies - Jobs - Locations", fontsize=10)
    plt.title("Max Salaries for Different Job Titles", fontsize=10)
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.legend()
    plt.savefig(
        "data_analysis/matplotlib_visuals/images/bar_plot.png", bbox_inches="tight"
    )
    plt.show()
    plt.close()


# Horizontal Bar Plot
def barh_plot(df):
    # Sort data by max_salaries
    df = df.sort_values(by="max_salaries", ascending=False)

    plt.figure(figsize=(15, 8))
    plt.barh(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["max_salaries"],
        label="Max Salaries",
        color=random.choice(colors),
    )
    plt.barh(
        df["company_names"]
        + " - "
        + df["job_titles"]
        + ": "
        + df["locations"]
        + " / "
        + difference["difference"],
        df["starting_salaries"],
        label="Starting Salaries",
        color=random.choice(colors),
    )
    plt.xlabel("Max Salaries Based on Country Code", fontsize=10)
    plt.ylabel("Companies - Jobs - Locations", fontsize=10)
    plt.title("Max Salaries for Different Job Titles", fontsize=10)
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest salary at the top
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.legend()
    plt.savefig(
        "data_analysis/matplotlib_visuals/images/barh_plot.png", bbox_inches="tight"
    )
    plt.show()
    plt.close()


line_plot(df)
bar_plot(df)
barh_plot(df)

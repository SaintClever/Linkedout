import random
from data_analysis.matplotlib_visuals.colors import colors
import pandas as pd
import matplotlib.pyplot as plt
from .generate_df import df


def create_plot(df):
    differ = [
        f"{max_salary - df['starting_salary'][i]:,}"
        for i, max_salary in enumerate(df["max_salary"])
    ]

    difference = pd.DataFrame({"difference": differ})

    fig, ax = plt.subplots(figsize=(15, 8))

    ax.barh(
        df["company_name"]
        + " - "
        + df["job_title"]
        + ": "
        + df["location"]
        + " / "
        + difference["difference"],
        df["max_salary"],
        label="Max Salary",
        color=random.choice(colors),
        height=0.4,
    )

    ax.barh(
        df["company_name"]
        + " - "
        + df["job_title"]
        + ": "
        + df["location"]
        + " / "
        + difference["difference"],
        df["starting_salary"],
        label="Starting Salary",
        color=random.choice(colors),
        height=0.4,
    )

    ax.set_yticks(
        df["company_name"]
        + " - "
        + df["job_title"]
        + ": "
        + df["location"]
        + " / "
        + difference["difference"]
    )

    ax.set_xlabel("Salaries")
    ax.set_ylabel("Companies - Jobs - Locations")
    ax.grid()
    ax.legend()
    plt.tight_layout()
    plt.close("all")

    return fig


salary_plot = create_plot(df)

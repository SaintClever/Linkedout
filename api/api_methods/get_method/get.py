import random
from data_analysis.matplotlib_visuals.colors import colors
import matplotlib.pyplot as plt
from .generate_df import df


def create_plot(df):
    fig, ax = plt.subplots(figsize=(15, 8))

    ax.barh(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
        df["max_salaries"],
        label="Max Salaries",
        color=random.choice(colors),
        height=0.4,
    )

    ax.barh(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"],
        df["starting_salaries"],
        label="Starting Salaries",
        color=random.choice(colors),
        height=0.4,
    )

    ax.set_yticks(
        df["company_names"] + " - " + df["job_titles"] + ": " + df["locations"]
    )

    ax.set_xlabel("Salaries")
    ax.set_ylabel("Companies - Jobs - Locations")
    ax.grid()
    ax.legend()
    plt.tight_layout()
    plt.close("all")

    return fig


salary_plot = create_plot(df)

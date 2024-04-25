from .data_manipulation import df, df_aggregated

# Pre-cleaned data to CSV
df.to_csv("data_analysis/pandas_data/processed_job_data.csv", index=False)

# Aggregated data to csv
df_aggregated.to_csv(
    "data_analysis/pandas_data/processed_agg_job_data.csv", index=False
)
print("\ndata created: processed_job_data.csv\n")

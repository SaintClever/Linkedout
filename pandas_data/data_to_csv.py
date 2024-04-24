from .data_manipulation import df_aggregated

# To save to CSV
df_aggregated.to_csv("pandas_data/processed_job_data.csv", index=False)

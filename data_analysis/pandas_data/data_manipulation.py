from database.database import engine
import pandas as pd


connection = f"postgresql://{engine["pguser"]}:{engine["pgpassword"]}@{engine["pghost"]}/{engine["pgdatabase"]}?sslmode=require"

# Standard pre-cleaned data
def request_data_to_dataframe(connection):
    query = "SELECT * FROM jobs;"
    dataframe = pd.read_sql_query(query, connection)
    
    return dataframe


df = request_data_to_dataframe(connection)
# print(df.head())

# Aggregated_data
def aggregate_data(dataframe):
    aggregated_df = (
        dataframe.groupby("location")
        .agg({"max_salary": ["sum", "mean", "max", "std"]})
        .fillna(0)
        .reset_index()
    )

    aggregated_df["max_salary"] = aggregated_df["max_salary"].round(2)
    
    return aggregated_df


df_aggregated = aggregate_data(df)
print(df_aggregated)

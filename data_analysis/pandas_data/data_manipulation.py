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

import pandas as pd

def write():
    pass

def read(table: str):
    file = open(f"./src/storage/data/{table}.csv", 'r')
    data = file.read()

    return data

def read_pandas(table: str) -> pd.DataFrame:
    return pd.read_csv(f"./src/storage/data/{table}.csv")
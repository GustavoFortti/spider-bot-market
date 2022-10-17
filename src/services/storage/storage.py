import os
import pandas as pd

LOCAL_DATA_PATH = './src/services/storage/data/'

def write():
    pass

def read(table: str):
    file = open(f"{LOCAL_DATA_PATH}{table}.csv", 'r')
    data = file.read()

    return data

def read_pandas(table: str) -> pd.DataFrame:
    return pd.read_csv(f"{LOCAL_DATA_PATH}{table}.csv")
    
def write_pandas(data: str) -> None:
    pass
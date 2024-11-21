import pandas as pd

NC_FILE_PATH = "../data/results_pct_20241105.txt"

def read_data():
    df = pd.read_csv(NC_FILE_PATH, delimiter="\t")
    return df

def unique(df, column: str, sub_str: str):
    "Finds unique items in given column."
    return [item for item in df[column].unique() if sub_str in item]
    
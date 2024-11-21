import pandas as pd

NC_FILE_PATH = "../data/results_pct_20241105.txt"

def read_data():
    df = pd.read_csv(NC_FILE_PATH, delimiter="\t")
    return df

def unique(df, column: str, sub_str: str):
    "Finds unique items in given column."
    return [item for item in df[column].unique() if sub_str in item]
    
def filter_for(df, column, value):
    return df[df[column]==value]


def total_votes_per_precinct(df):
    return df.groupby("Precinct")[["Early Voting", "Total Votes"]].sum()


def filter_isin(df, column, values):
    return df[df[column].isin(values)]
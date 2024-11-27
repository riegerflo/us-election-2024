import pandas as pd

NC_FILE_PATH = "../data/results_pct_20241105.txt"

def read_data(path=NC_FILE_PATH):
    df = pd.read_csv(path, delimiter="\t")
    return df

def unique(df, column: str, sub_str: str):
    "Finds unique items in given column."
    return [item for item in df[column].unique() if sub_str in item]
    
def filter_for(df, column, value):
    return df[df[column]==value]


def contains(df, column, substr):
    return df[df[column].str.contains(substr)]


def total_votes_per_precinct(df):
    return df.groupby("Precinct")[["Early Voting", "Total Votes"]].sum()


def filter_isin(df, column, values):
    return df[df[column].isin(values)]


def filter_multiindex_by_tuples(df, filter_tuples):
    """
    Filter a pandas DataFrame with a MultiIndex based on a list of index tuples.
    
    Parameters:
    - df: The pandas DataFrame with a MultiIndex.
    - filter_tuples: A list of tuples, where each tuple corresponds to a specific 
                      combination of index values to keep.
                    
    Returns:
    - A filtered DataFrame.
    """
    # Create a list of tuples to match in the MultiIndex
    filtered_df = df[df.index.isin(filter_tuples)]
    
    return filtered_df

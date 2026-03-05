import pandas as pd

def load_data(filepath:str) -> pd.DataFrame:
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame

    TODO: Unless done in a different func., handle incorrect values
    """
    df = pd.read_csv(filepath, parse_dates=['order_date'])
    # handle missing values by dropping the row if it contains a NaN
    df.dropna(inplace=True)
    return df

def explore_data(df:pd.DataFrame) -> None:
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    # i know the formatting here is terrible, but the headers will not print out 
    # looking good unless it looks like this mess
    print(f"""
--- Shape of the dataset ---\n{df.shape}\n\n
--- Data types ---\n{df.dtypes}\n\n
--- Missing values ---\n{df.isnull().sum()}\n\n
--- Basic statistics for numeric columns ---\n{df.describe()}\n\n
--- Date range covered ---\n{df['order_date'].min()} to {df['order_date'].max()}
""")

df = load_data('starter_code/orders.csv')
explore_data(df)
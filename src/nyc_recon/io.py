import pandas as pd

def load_payroll_csv(path: str) -> pd.DataFrame:
    """
    Load a payroll CSV file into a pandas DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """

    return pd.read_csv(path)

def load_spending_csv(path: str) -> pd.DataFrame:
    """
    Load a spending CSV file into a pandas DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """

    return pd.read_csv(path)
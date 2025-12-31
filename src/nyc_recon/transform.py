import pandas as pd
from nyc_recon.cleaning import normalize_agency_name

def clean_payroll_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the payroll DataFrame by stripping whitespace from string columns and
    formatting/verifying numeric values.
    Args:
        df (pd.DataFrame): The payroll DataFrame to clean.
    Returns:
        pd.DataFrame: The cleaned payroll DataFrame.
    """

    df = df.copy()

    return (
        df
        .assign(
            agency_key=lambda d: d["Agency"].map(normalize_agency_name),
            fiscal_year=lambda d: pd.to_numeric(d["FiscalYear"], errors="raise"),
            total_pay=lambda d: pd.to_numeric(
                d["TotalPay"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False), 
                errors="raise"
            ),
        )
        .loc[:, ["agency_key", "fiscal_year", "total_pay"]]
        .assign(
            fiscal_year=lambda d: d["fiscal_year"].astype(int),
            total_pay=lambda d: d["total_pay"].astype(float),
        )
    )

def clean_spending_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the spending DataFrame by stripping whitespace from string columns and
    formatting/verifying numeric values.
    Args:
        df (pd.DataFrame): The spending DataFrame to clean.
    Returns:
        pd.DataFrame: The cleaned spending DataFrame.
    """

    df = df.copy()

    return (
        df
        .assign(
            agency_key=lambda d: d["Agency"].map(normalize_agency_name),
            fiscal_year=lambda d: pd.to_numeric(d["FiscalYear"], errors="raise"),
            total_spending=lambda d: pd.to_numeric(
                d["TotalSpending"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False), 
                errors="raise"
            ),
        )
        .loc[:, ["agency_key", "fiscal_year", "total_spending"]]
        .assign(
            fiscal_year=lambda d: d["fiscal_year"].astype(int),
            total_spending=lambda d: d["total_spending"].astype(float),
        )
    )
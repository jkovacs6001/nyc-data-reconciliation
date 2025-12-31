import pandas as pd
from nyc_recon.io import load_payroll_csv, load_spending_csv
import pytest
from pathlib import Path

@pytest.fixture
def data_dir() -> Path:
    """Fixture that provides the path to the data fixtures directory."""
    return Path(__file__).parent.parent / "data" / "fixtures"

@pytest.fixture
def payroll_df(data_dir) -> pd.DataFrame:
    """Fixture that loads the payroll CSV into a DataFrame."""
    return load_payroll_csv(data_dir / "payroll_sample.csv")

@pytest.fixture
def spending_df(data_dir) -> pd.DataFrame:
    """Fixture that loads the spending CSV into a DataFrame."""
    return load_spending_csv(data_dir / "spending_sample.csv")

## Payroll CSV Tests

def test_payroll_columns_present(payroll_df):
    """Test that the payroll CSV contains the expected columns."""

    expected_columns = {"Agency", "FiscalYear", "TotalPay"}
    assert expected_columns.issubset(set(payroll_df.columns))

def test_payroll_agency_names_not_empty(payroll_df):
    """Test that the 'Agency' column in the payroll CSV is populated with non-empty strings."""

    assert (payroll_df["Agency"].astype(str).str.strip() != "").all()

def test_payroll_fiscal_years_parseable_to_int_and_present(payroll_df):
    """Test that the 'FiscalYear' column in the payroll CSV can be parsed to integers."""

    fiscal_years = payroll_df["FiscalYear"]
    parsed = pd.to_numeric(fiscal_years, errors='coerce')

    assert parsed.notna().all()
    assert (parsed % 1 == 0).all()

def test_payroll_totals_parseable_after_cleanup(payroll_df):
    """Test that the 'TotalPay' column in the payroll CSV can be parsed to floats after cleanup."""

    payroll_totals = payroll_df["TotalPay"].astype(str).str.replace(",", "", regex=False).str.replace("$", "", regex=False)
    parsed = pd.to_numeric(payroll_totals, errors='coerce')
    assert parsed.notna().all()

## Spending CSV Tests

def test_spending_columns_present(spending_df):
    """Test that the spending CSV contains the expected columns."""

    expected_columns = {"Agency", "FiscalYear", "TotalSpending"}
    assert expected_columns.issubset(set(spending_df.columns))

def test_spending_agency_names_not_empty(spending_df):
    """Test that the 'Agency' column in the spending CSV is populated with non-empty strings."""

    assert (spending_df["Agency"].astype(str).str.strip() != "").all()

def test_spending_fiscal_years_parseable_to_int_and_present(spending_df):
    """Test that the 'FiscalYear' column in the spending CSV can be parsed to integers."""

    fiscal_years = spending_df["FiscalYear"]
    parsed = pd.to_numeric(fiscal_years, errors='coerce')
    
    assert parsed.notna().all()
    assert (parsed % 1 == 0).all()

def test_spending_totals_parseable_after_cleanup(spending_df):
    """Test that the 'TotalSpending' column in the spending CSV can be parsed to floats after cleanup."""

    spending_totals = spending_df["TotalSpending"].astype(str).str.replace(",", "", regex=False).str.replace("$", "", regex=False)
    parsed = pd.to_numeric(spending_totals, errors='coerce')
    assert parsed.notna().all()
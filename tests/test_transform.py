from nyc_recon.transform import clean_payroll_data, clean_spending_data
import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture
def data_dir() -> str:
    """Fixture that provides the path to the data fixtures directory."""
    return Path(__file__).parent.parent / "data" / "fixtures"

@pytest.fixture
def cleaned_payroll_df(data_dir) -> pd.DataFrame:
    """Fixture that provides the cleaned payroll DataFrame."""
    raw_df = pd.read_csv(data_dir / "payroll_sample.csv")
    return clean_payroll_data(raw_df)

@pytest.fixture
def cleaned_spending_df(data_dir) -> pd.DataFrame:
    """Fixture that provides the cleaned spending DataFrame."""
    raw_df = pd.read_csv(data_dir / "spending_sample.csv")
    return clean_spending_data(raw_df)

# Payroll DataFrame Tests

def test_payroll_expected_columns(cleaned_payroll_df):
    """Test that the cleaned payroll DataFrame contains only the expected columns."""
    expected_columns = {"agency_key", "fiscal_year", "total_pay"}
    assert set(cleaned_payroll_df.columns) == expected_columns

def test_payroll_fiscal_years_as_int(cleaned_payroll_df):
    """Test that the 'fiscal_year' column in the cleaned payroll DataFrame is of integer type."""
    assert pd.api.types.is_integer_dtype(cleaned_payroll_df["fiscal_year"])

def test_payroll_total_pay_as_float(cleaned_payroll_df):
    """Test that the 'total_pay' column in the cleaned payroll DataFrame is of float type."""
    assert pd.api.types.is_float_dtype(cleaned_payroll_df["total_pay"])

# Spending DataFrame Tests

def test_spending_expected_columns(cleaned_spending_df):
    """Test that the cleaned spending DataFrame contains only the expected columns."""
    expected_columns = {"agency_key", "fiscal_year", "total_spending"}
    assert set(cleaned_spending_df.columns) == expected_columns

def test_spending_fiscal_years_as_int(cleaned_spending_df):
    """Test that the 'fiscal_year' column in the cleaned spending DataFrame is of integer type."""
    assert pd.api.types.is_integer_dtype(cleaned_spending_df["fiscal_year"])

def test_spending_total_spending_as_float(cleaned_spending_df):
    """Test that the 'total_spending' column in the cleaned spending DataFrame is of float type."""
    assert pd.api.types.is_float_dtype(cleaned_spending_df["total_spending"])

# Cross-dataset Tests
def test_agency_keys_match(cleaned_payroll_df, cleaned_spending_df):
    """Test that the agency keys in both cleaned DataFrames match."""
    payroll_agencies = set(cleaned_payroll_df["agency_key"].unique())
    spending_agencies = set(cleaned_spending_df["agency_key"].unique())
    assert payroll_agencies == spending_agencies
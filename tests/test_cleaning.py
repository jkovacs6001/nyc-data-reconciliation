import pytest
from nyc_recon.cleaning import normalize_agency_name

@pytest.fixture
def global_agency_name() -> str:
    """Fixture that provides a sample agency name with extra whitespace and mixed case."""
    return "  Department of\tTransportation  "

def test_trims_left_whitespace(global_agency_name):
    """Test that the agency name has no leading whitespace."""

    result = normalize_agency_name(global_agency_name)
    assert result and not result[:1].isspace()

def test_trims_right_whitespace(global_agency_name):
    """Test that the agency name has no trailing whitespace."""

    result = normalize_agency_name(global_agency_name)
    assert result and not result[-1:].isspace()

def test_preserves_tokens(global_agency_name):
    """Test that the order of tokens in the agency name is preserved."""
    
    result = normalize_agency_name(global_agency_name)
    assert result.lower().split() == global_agency_name.lower().split()

def test_internal_whitespace_normalized(global_agency_name):
    """Test that internal whitespace characters are normalized to single spaces."""
    
    result = normalize_agency_name(global_agency_name)
    assert "  " not in result # No double spaces
    assert "\t" not in result
    assert "\n" not in result

def test_to_lowercase(global_agency_name):
    """Test that the agency name is converted to lowercase."""
    
    result = normalize_agency_name(global_agency_name)
    assert result == result.lower()

def test_only_whitespace_name():
    """Test that an agency name consisting only of whitespace is normalized to an empty string."""
    
    result = normalize_agency_name("     \t   \n  ")
    assert result == ""

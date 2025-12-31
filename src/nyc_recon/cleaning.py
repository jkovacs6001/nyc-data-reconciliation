def normalize_agency_name(name: str) -> str:
    """
    Normalize an agency name for use as a reconciliation key.

    Guarantees:
    - no leading or trailing whitespace
    - lowercase
    - internal whitespace collapsed to single spaces
    - token order preserved

    Args:
        name (str): The original agency name.

    Returns:
        str: The normalized agency name.
    """
    
    return " ".join(name.strip().lower().split())
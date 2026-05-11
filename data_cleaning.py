import re
import pandas as pd

def clean_whitespace(data):
    """Removes leading/trailing whitespace from strings in a list."""
    return [item.strip() for item in data if isinstance(item, str)]

def remove_empty_entries(data):
    """Removes empty strings and None values from a list."""
    return [item for item in data if item not in ("", None)]

def standardize_case(data, case="lower"):
    """Standardizes string case in a list."""
    if case == "lower":
        return [item.lower() for item in data if isinstance(item, str)]
    elif case == "upper":
        return [item.upper() for item in data if isinstance(item, str)]
    return data

def remove_special_characters(data):
    """Removes special characters from strings in a list."""
    return [re.sub(r'[^A-Za-z0-9 ]+', '', item) for item in data if isinstance(item, str)]

def drop_duplicates(data):
    """Removes duplicate entries from a list."""
    return list(set(data))

def clean_dataframe(df):
    """Performs basic cleaning on a pandas DataFrame."""
    df = df.dropna()  # Remove rows with missing values
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]  # Clean column names
    return df



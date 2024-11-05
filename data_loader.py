import pandas as pd

def load_data(file_path):
    """Loads the CSV file into a DataFrame with error handling."""
    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: There was a parsing issue with the file at {file_path}.")
        return None

def save_data(df, file_path):
    """Saves the DataFrame to a CSV file."""
    if df is not None:
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    else:
        print("No data to save.")

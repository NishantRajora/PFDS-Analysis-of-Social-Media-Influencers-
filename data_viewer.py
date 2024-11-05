def view_data(df, rows=5):
    """Displays the first few rows of the DataFrame."""
    if df is not None:
        print(df.head(rows))
    else:
        print("No data to display.")

def show_statistics(df):
    """Displays summary statistics for numerical columns in the DataFrame."""
    if df is not None:
        print(df.describe())
    else:
        print("No data to display statistics for.")

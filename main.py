from data_loader import load_data, save_data
from data_viewer import view_data, show_statistics
from data_manager import add_influencer

def main():
    file_path = 'indian_influencers_data.csv'  # Path to your CSV file
    
    # Load data
    df = load_data(file_path)
    
    # View data
    if df is not None:
        print("Loaded Data:")
        view_data(df)

        # Show statistics
        print("\nSummary Statistics:")
        show_statistics(df)
    
        # Add a new influencer to the data
        df = add_influencer(
            df, 
            influencer_name="NewStar", 
            platform="Instagram", 
            follower_count=1000000, 
            likes=80000, 
            shares=5000, 
            comments=3000, 
            post_frequency=15, 
            content_type="fashion"
        )

        # View updated data
        print("\nUpdated Data:")
        view_data(df)

        # Save updated data
        save_data(df, file_path)

# Run the main function
if __name__ == "__main__":
    main()

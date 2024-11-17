import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV file
def load_data(filename='influencers.csv'):
    try:
        data = pd.read_csv(filename)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Creating a new one.")
        data = pd.DataFrame(columns=[
            'influencer_name', 'platform', 'follower_count', 'content_type', 
            'post_frequency', 'likes_2020', 'likes_2021', 'likes_2022', 'likes_2023', 
            'likes_2024', 'shares_2020', 'shares_2021', 'shares_2022', 'shares_2023', 
            'shares_2024', 'comments_2020', 'comments_2021', 'comments_2022', 
            'comments_2023', 'comments_2024'
        ])
    return data

# Display the data
def show_data(data):
    print("\nData from CSV file:")
    print(data)

# Display summary of the dataset (only showing names, platform, and content_type)
def show_summary(data):
    # Calculate average likes, comments, and shares across 2020-2024 for each influencer
    data['avg_likes'] = data[['likes_2020', 'likes_2021', 'likes_2022', 'likes_2023', 'likes_2024']].mean(axis=1)
    data['avg_comments'] = data[['comments_2020', 'comments_2021', 'comments_2022', 'comments_2023', 'comments_2024']].mean(axis=1)
    data['avg_shares'] = data[['shares_2020', 'shares_2021', 'shares_2022', 'shares_2023', 'shares_2024']].mean(axis=1)
    
    # Create the summary DataFrame including the new average columns
    summary = data[['influencer_name', 'platform', 'content_type', 'avg_likes', 'avg_comments', 'avg_shares']]
    
    print("\nSummary (Influencer Name, Platform, Content Type, Average Likes, Comments, and Shares):")
    print(summary)

# Add new data
def add_data(data):
    new_data = {
        'influencer_name': input("Enter Influencer Name: "),
        'platform': input("Enter Platform: "),
        'follower_count': int(input("Enter Follower Count: ")),
        'content_type': input("Enter Content Type: "),
        'post_frequency': int(input("Enter Post Frequency: ")),
        'likes_2020': int(input("Enter Likes in 2020: ")),
        'likes_2021': int(input("Enter Likes in 2021: ")),
        'likes_2022': int(input("Enter Likes in 2022: ")),
        'likes_2023': int(input("Enter Likes in 2023: ")),
        'likes_2024': int(input("Enter Likes in 2024: ")),
        'shares_2020': int(input("Enter Shares in 2020: ")),
        'shares_2021': int(input("Enter Shares in 2021: ")),
        'shares_2022': int(input("Enter Shares in 2022: ")),
        'shares_2023': int(input("Enter Shares in 2023: ")),
        'shares_2024': int(input("Enter Shares in 2024: ")),
        'comments_2020': int(input("Enter Comments in 2020: ")),
        'comments_2021': int(input("Enter Comments in 2021: ")),
        'comments_2022': int(input("Enter Comments in 2022: ")),
        'comments_2023': int(input("Enter Comments in 2023: ")),
        'comments_2024': int(input("Enter Comments in 2024: "))
    }
    # Convert the dictionary to a DataFrame and use pd.concat to add it
    new_data_df = pd.DataFrame([new_data])
    data = pd.concat([data, new_data_df], ignore_index=True)
    print("\nNew data added successfully.")
    return data

# Save data back to CSV
def save_data(data, filename='influencers.csv'):
    data.to_csv(filename, index=False)
    print("Data saved to", filename)

# Plot Likes, Comments, Shares across Years (2020-2024)
def plot_graph(data, influencer_name):
    influencer_data = data[data['influencer_name'] == influencer_name]
    
    if influencer_data.empty:
        print(f"No data found for influencer: {influencer_name}")
        return

    years = ['2020', '2021', '2022', '2023', '2024']
    
    likes = [influencer_data[f'likes_{year}'].values[0] for year in years]
    comments = [influencer_data[f'comments_{year}'].values[0] for year in years]
    shares = [influencer_data[f'shares_{year}'].values[0] for year in years]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, likes, label='Likes', marker='o')
    plt.plot(years, comments, label='Comments', marker='o')
    plt.plot(years, shares, label='Shares', marker='o')

    plt.title(f'Likes, Comments, and Shares for {influencer_name} (2020-2024)')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot Follower Counts for Different Influencers
def plot_follower_counts(data):
    # Select influencers and their follower counts
    if data.empty:
        print("No data available to plot.")
        return
    
    # Sort by follower count to make the chart more readable (optional)
    sorted_data = data.sort_values(by='follower_count', ascending=False)
    
    # Get influencer names and follower counts
    influencer_names = sorted_data['influencer_name']
    follower_counts = sorted_data['follower_count']
    
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.bar(influencer_names, follower_counts, color='skyblue')
    plt.title("Follower Counts of Influencers")
    plt.xlabel("Influencer")
    plt.ylabel("Follower Count")
    plt.xticks(rotation=45, ha='right')  # Rotate names for better readability
    plt.tight_layout()  # Adjust layout to avoid cutoff labels
    plt.show()

def main():
    data = load_data()
    while True:
        print("\n--- Influencer Data Management ---")
        print("1. Show Data")
        print("2. Show Summary")
        print("3. Add Data")
        print("4. Save Data")
        print("5. Plot Likes, Comments, and Shares for an Influencer")
        print("6. Show Follower Counts of Influencers (Bar Graph)")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_data(data)
        elif choice == '2':
            show_summary(data)
        elif choice == '3':
            data = add_data(data)
        elif choice == '4':
            save_data(data)
        elif choice == '5':
            influencer_name = input("Enter the Influencer Name to plot graph: ")
            plot_graph(data, influencer_name)
        elif choice == '6':
            plot_follower_counts(data)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


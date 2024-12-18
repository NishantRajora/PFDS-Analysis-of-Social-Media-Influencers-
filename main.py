import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

def show_data(data):
    print("\nData from CSV file:")
    print(data)

def show_summary(data):
    data['avg_likes'] = data[['likes_2020', 'likes_2021', 'likes_2022', 'likes_2023', 'likes_2024']].mean(axis=1)
    data['avg_comments'] = data[['comments_2020', 'comments_2021', 'comments_2022', 'comments_2023', 'comments_2024']].mean(axis=1)
    data['avg_shares'] = data[['shares_2020', 'shares_2021', 'shares_2022', 'shares_2023', 'shares_2024']].mean(axis=1)

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
    data = data.append(new_data, ignore_index=True)
    print("\nNew data added successfully.")
    return data

def save_data(data, filename='influencers.csv'):
    data.to_csv(filename, index=False)
    print("Data saved to", filename)


def plot_graph(data, influencer_name):
    influencer_data = data[data['influencer_name'] == influencer_name]
    
    if influencer_data.empty:
        print(f"No data found for influencer: {influencer_name}")
        return

    years = ['2020', '2021', '2022', '2023', '2024']
    
    likes = [influencer_data[f'likes_{year}'].values[0] for year in years]
    comments = [influencer_data[f'comments_{year}'].values[0] for year in years]
    shares = [influencer_data[f'shares_{year}'].values[0] for year in years]

    plt.figure(figsize=(10, 6))
    plt.plot(years, likes, label='Likes', marker='o',linestyle='--')
    plt.plot(years, comments, label='Comments', marker='o')
    plt.plot(years, shares, label='Shares', marker='o')

    plt.title(f'Likes, Comments, and Shares for {influencer_name} (2020-2024)')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_follower_counts(data):

    if data.empty:
        print("No data available to plot.")
        return
    
    sorted_data = data.sort_values(by='follower_count', ascending=False)

    influencer_names = sorted_data['influencer_name']
    follower_counts = sorted_data['follower_count']

    plt.figure(figsize=(14, 7))
    plt.bar(influencer_names, follower_counts, color='blue')
    plt.title("Follower Counts ")
    plt.xlabel("Influencer")
    plt.ylabel("Follower Count")
    plt.xticks(rotation=90, ha='left')   
    plt.show()




def main():
    data = load_data()
    while True:
        print("\ Influencer Analysis ")
        print("1. Show Data")
        print("2. Show Summary")
        print("3. Add Data")
        print("4. Save Data")
        print("5. Plot Likes, Comments, and Shares for Influencer")
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
            influencer_name = input("Enter the Influencer Name ")
            plot_graph(data, influencer_name)
        elif choice == '6':
            plot_follower_counts(data)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

import pandas as pd

# Creating a sample data dictionary with growth projections for Tech Burner.
# Similar data can be generated for other influencers as well if needed.

data = {
    "influencer_name": [
        "Tech Burner", "Paras", "Nirjhar", "Umang", "ComedyKing",
        "Indian bagpaker", "Preyansh", "Deepanshu", "Monika", "Piyush"
    ],
    "platform": [
        "YouTube", "Instagram", "Instagram", "YouTube", "YouTube",
        "Instagram", "Instagram", "YouTube", "YouTube", "Instagram"
    ],
    "follower_count": [
        5000000, 2000000, 3500000, 1000000, 5500000,
        1800000, 1500000, 3000000, 2500000, 1700000
    ],
    "content_type": [
        "tech", "fitness", "fashion", "food", "comedy",
        "travel", "beauty", "dance", "lifestyle", "gaming"
    ],
    "post_frequency": [
        20, 25, 30, 15, 40,
        18, 22, 28, 15, 24
    ],
    "likes_2020": [
        180000, 120000, 140000, 80000, 400000,
        100000, 90000, 150000, 120000, 110000
    ],
    "likes_2021": [
        220000, 135000, 160000, 90000, 450000,
        110000, 100000, 175000, 130000, 120000
    ],
    "likes_2022": [
        250000, 145000, 180000, 95000, 470000,
        115000, 105000, 200000, 140000, 125000
    ],
    "likes_2023": [
        300000, 150000, 200000, 100000, 500000,
        120000, 110000, 225000, 150000, 130000
    ],
    "likes_2024": [
        320000, 160000, 220000, 110000, 520000,
        125000, 115000, 250000, 160000, 135000
    ],
    "shares_2020": [
        30000, 8000, 7000, 5000, 20000,
        9000, 6000, 12000, 10000, 9000
    ],
    "shares_2021": [
        35000, 8500, 8000, 5500, 22000,
        9500, 6500, 14000, 11000, 10000
    ],
    "shares_2022": [
        40000, 9000, 8500, 6000, 25000,
        10000, 7000, 16000, 12000, 11000
    ],
    "shares_2023": [
        50000, 9500, 9000, 6000, 30000,
        11000, 7500, 18000, 13000, 12000
    ],
    "shares_2024": [
        55000, 10000, 9500, 6500, 32000,
        12000, 8000, 20000, 14000, 12500
    ],
    "comments_2020": [
        12000, 4000, 5000, 3000, 15000,
        3500, 2500, 7000, 6000, 5000
    ],
    "comments_2021": [
        15000, 4500, 6000, 3500, 17000,
        4000, 3000, 8000, 6500, 5500
    ],
    "comments_2022": [
        17000, 5000, 6500, 4000, 20000,
        4500, 3500, 9000, 7000, 6000
    ],
    "comments_2023": [
        20000, 5000, 7000, 4500, 25000,
        5000, 4000, 10000, 7500, 6500
    ],
    "comments_2024": [
        22000, 5500, 7500, 5000, 27000,
        5500, 4500, 11000, 8000, 7000
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Saving to CSV
file_path = "influencer_growth_data.csv"
df.to_csv(file_path, index=False)

file_path

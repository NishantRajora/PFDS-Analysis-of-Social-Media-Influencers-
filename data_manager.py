def add_influencer(df, influencer_name, platform, follower_count, likes, shares, comments, post_frequency, content_type):
    """Adds a new influencer's data to the DataFrame."""
    new_data = {
        'influencer_name': influencer_name,
        'platform': platform,
        'follower_count': follower_count,
        'likes': likes,
        'shares': shares,
        'comments': comments,
        'post_frequency': post_frequency,
        'content_type': content_type
    }
    df = df.append(new_data, ignore_index=True)
    print(f"Added influencer: {influencer_name}")
    return df

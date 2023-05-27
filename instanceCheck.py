import praw
import pandas as pd
import datetime as dt
import re
from pmaw import PushshiftAPI

# Read symbols.csv
symbols_df = pd.read_csv('unique_symbols.csv')

# Reddit API credentials
reddit = praw.Reddit(client_id='ogFrhC2M8F9dEZf1pQiwbw',
                     client_secret='r0E5cVRtSps_DHZaAQkD0Yi6Qalkuw',
                     user_agent='my_reddit_data_fetcher:v1.0 (by /u/Pstaboche)')

# Set up the Pushshift API using PMAW
api = PushshiftAPI()

# Define the subreddit to scrape
subreddit_name = 'wallstreetbets'

# Define the time range
start_date = int(dt.datetime(2017, 1, 1).timestamp())
end_date = int(dt.datetime(2017, 12, 31).timestamp())

# Use the 'search_submissions' method from PMAW to fetch posts within the time range
submissions = list(api.search_submissions(after=start_date, before=end_date, subreddit=subreddit_name))

print(f"Fetched {len(submissions)} submissions")

# Initialize a dictionary to store the symbol counts
symbol_counts = {}

# Iterate over the submissions
for submission in submissions:
    post_title = submission['title'].lower()

    # Check if any symbol from symbols.csv is present in the post title
    for symbol in symbols_df['Symbol']:
        pattern = r'\b' + re.escape(symbol) + r'\b'
        if re.search(pattern, post_title, re.IGNORECASE):
            # Increment the symbol count in the dictionary
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1

# Convert the symbol_counts dictionary to a DataFrame
symbol_counts_df = pd.DataFrame(list(symbol_counts.items()), columns=['Symbol', 'Count'])

# Save the symbol counts data to a CSV file
symbol_counts_df.to_csv('symbol_counts.csv', index=False)

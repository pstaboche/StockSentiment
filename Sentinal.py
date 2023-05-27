import praw
import pandas as pd
import datetime as dt
from pmaw import PushshiftAPI

# Read symbols.csv
symbols_df = pd.read_csv('symbols.csv')

# Reddit API credentials
reddit = praw.Reddit(client_id = 'ogFrhC2M8F9dEZf1pQiwbw',
                     client_secret = 'r0E5cVRtSps_DHZaAQkD0Yi6Qalkuw',
                     user_agent = 'my_reddit_data_fetcher:v1.0 (by /u/Pstaboche)')

# Set up the Pushshift API using PMAW
api = PushshiftAPI()

# Define subreddits to scrape
subreddits = ['stocks', 'investing', 'wallstreetbets']

# Define the time range
start_date = int(dt.datetime(2012, 1, 31).timestamp())
end_date = int(dt.datetime(2018, 1, 1).timestamp())

# Initialize an empty DataFrame to store the collected data
data = []

# Loop through the subreddits
for subreddit_name in subreddits:
    # Use the 'search_submissions' method from PMAW to fetch posts within the time range
    for submission in api.search_submissions(after=start_date, before=end_date, subreddit=subreddit_name):
        post_title = submission.title.lower()

        # Check if any symbol from symbols.csv is present in the post title
        for symbol in symbols_df['symbol']:
            if symbol.lower() in post_title:
                post_data = {
                    'symbol': symbol,
                    'subreddit': subreddit_name,
                    'title': submission.title,
                    'text': submission.selftext,
                    'timestamp': submission.created_utc,
                    'upvotes': submission.ups,
                    'downvotes': submission.downs,
                    'num_comments': submission.num_comments
                }

                # Add the post data to the data list
                data.append(post_data)
                break

# Convert the data list to a DataFrame
data_df = pd.DataFrame(data)

# Save the collected data to a CSV file
data_df.to_csv('reddit_stock_posts.csv', index=False)

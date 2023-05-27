import praw
import pandas as pd
import datetime as dt
import re
from pmaw import PushshiftAPI

# Read symbols.csv
symbols_df = pd.read_csv('symbols.csv')

# Reddit API credentials
reddit = praw.Reddit(client_id='ogFrhC2M8F9dEZf1pQiwbw',
                     client_secret='r0E5cVRtSps_DHZaAQkD0Yi6Qalkuw',
                     user_agent='my_reddit_data_fetcher:v1.0 (by /u/Pstaboche)')

# Set up the Pushshift API using PMAW
api = PushshiftAPI()

# Define subreddits to scrape
subreddits = ['stocks', 'investing', 'wallstreetbets']

# Define the time range
initial_start_date = int(dt.datetime(2017, 1, 1).timestamp())
end_date = int(dt.datetime(2017, 1, 31).timestamp())

# Loop through the subreddits
for subreddit_name in subreddits:
    start_date = initial_start_date
    data = []

    while start_date < end_date:
        # Use the 'search_submissions' method from PMAW to fetch posts within the time range
        submissions = list(api.search_submissions(after=start_date, before=end_date, subreddit=subreddit_name, limit=500))

        print(f"Subreddit: {subreddit_name}, fetched: {len(submissions)} submissions")

        # Check if there are no more submissions available
        if not submissions:
            break

        # Update start_date to fetch the next batch of submissions
        start_date = submissions[-1]['created_utc']

        for submission in submissions:
            post_title = submission['title'].lower()

            # Check if any symbol from symbols.csv is present in the post title
            for symbol in symbols_df['Symbol']:
                # Use regular expressions to search for whole-word matches
                pattern = r'\b' + re.escape(symbol) + r'\b'
                if re.search(pattern, post_title, re.IGNORECASE):
                    print(f"Matched '{symbol}' in post title: {post_title}")

                    post_data = {
                        'symbol': symbol,
                        'subreddit': subreddit_name,
                        'title': submission['title'],
                        'text': submission['selftext'],
                        'timestamp': submission['created_utc'],
                        'upvotes': submission['score'],
                        'num_comments': submission['num_comments']
                    }

                    # Add the post data to the data list
                    data.append(post_data)
                    break

    # Convert the data list to a DataFrame
    data_df = pd.DataFrame(data)

    # Save the collected data to a CSV file
    data_df.to_csv(f'{subreddit_name}_stock_posts.csv', index=False)

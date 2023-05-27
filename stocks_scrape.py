import datetime as dt
import pandas as pd
import re
from pmaw import PushshiftAPI

# Read symbols.csv
symbols_df = pd.read_csv('Symbols.csv')

# Define the time range
start_date = int(dt.datetime(2017, 1, 1).timestamp())
end_date = int(dt.datetime(2017, 11, 10).timestamp())

# Define the subreddit to fetch data from
subreddit_name = 'stocks'

# Initialize the Pushshift API
api = PushshiftAPI()

# Set the batch limit
batch_limit = 500
batch_after = start_date

# Initialize an empty list to store submissions
all_submissions = []

# Fetch submissions in batches
while batch_after < end_date:
    # Fetch a batch of submissions
    submissions = api.search_submissions(after=batch_after, before=end_date, subreddit=subreddit_name, limit=batch_limit)

    # Check if there are any submissions in the batch
    if not submissions:
        break

    # Filter submissions by checking if any symbol from symbols.csv is present in the post title
    filtered_submissions = []
    for submission in submissions:
        post_title = submission['title'].lower()
        
        for symbol in symbols_df['symbol']:
            pattern = re.compile(r'\b{}\b'.format(symbol.lower()))
            if pattern.search(post_title):
                filtered_submissions.append(submission)
                break

    # Add the filtered submissions from the current batch to the list of all submissions
    all_submissions.extend(filtered_submissions)

    # Update the timestamp for the next batch
    batch_after = submissions[-1]['created_utc']

print(f'Fetched {len(all_submissions)} submissions from r/{subreddit_name} containing symbols from Symbols.csv')

import time
import praw
from pmaw import PushshiftAPI
import csv

client_id = 'ogFrhC2M8F9dEZf1pQiwbw'
client_secret = 'r0E5cVRtSps_DHZaAQkD0Yi6Qalkuw'
user_agent = 'scraper:Market_Sentinal:V1.1 (by /u/pstaboche)'

# Create a list of ticker symbols
with open('unique_symbols.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    ticker_symbols = [row[0] for row in reader]

def get_date(date):
    return int(time.mktime(time.strptime(date, "%Y-%m-%d")))

start_date = get_date('2017-01-01')
end_date = get_date('2017-11-10')

api = PushshiftAPI()

# query submissions using PMAW
posts = api.search_submissions(subreddit='wallstreetbets', after=start_date, before=end_date, sort='desc', sort_type='score', limit=1000)

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

results = []
for post in posts:
    post_content = reddit.submission(id=post['id'])
    for ticker_symbol in ticker_symbols:
        if ticker_symbol.lower() in post_content.title.lower() or ticker_symbol.lower() in post_content.selftext.lower():
            results.append((ticker_symbol, post_content))

# Save the results to a CSV file
with open('wsb_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['ticker_symbol', 'title', 'post_content', 'upvotes', 'downvotes', 'num_comments', 'posting_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow({
            'ticker_symbol': result[0],
            'title': result[1].title,
            'post_content': result[1].selftext,
            'upvotes': result[1].ups,
            'downvotes': result[1].downs,
            'num_comments': result[1].num_comments,
            'posting_date': time.strftime('%Y-%m-%d', time.localtime(result[1].created))
        })

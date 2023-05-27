import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import datetime

# Load the data
data = pd.read_csv('/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/wsb_results.csv')

# Basic data exploration
print(f'Total rows: {data.shape[0]}')
print(f'Total columns: {data.shape[1]}')
print('Column names:')
print(data.columns)

# Check for null values
print('Null values:')
print(data.isnull().sum())

# Summary statistics for numerical columns
print('Summary statistics:')
print(data.describe())

# Distribution of upvotes
plt.figure(figsize=(10, 6))
plt.hist(data['upvotes'], bins=50, log=True)
plt.xlabel('Upvotes')
plt.ylabel('Frequency')
plt.title('Distribution of Upvotes')
plt.show()

# Wordcloud for title and body
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

title_text = ' '.join(data['title'])
body_text = ' '.join(data['body'])

print('Wordcloud for Title:')
create_wordcloud(title_text)

print('Wordcloud for Body:')
create_wordcloud(body_text)

# Best time to post (by upvotes)
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['hour'] = data['timestamp'].dt.hour
avg_upvotes_by_hour = data.groupby('hour')['upvotes'].mean().sort_values(ascending=False)
print('Best time to post (by average upvotes):')
print(avg_upvotes_by_hour.idxmax())

# Top 10 most upvoted posts
top_posts = data.sort_values('upvotes', ascending=False)[:10]
print('Top 10 most upvoted posts:')
print(top_posts[['title', 'upvotes']])

import pandas as pd
from convokit import Corpus, download

# Download three corpora
corpus1 = Corpus(filename=download("subreddit-wallstreetbets"))
corpus2 = Corpus(filename=download("subreddit-stocks"))
corpus3 = Corpus(filename=download("subreddit-investing"))

# Merge the corpora
merged_corpus = corpus1.merge(corpus2).merge(corpus3)

# Print summary stats for the merged corpus
merged_corpus.print_summary_stats()


# Convert corpus to dataframe
corpus_df = pd.DataFrame([utterance.meta for utterance in merged_corpus.iter_utterances()])

# Convert the timestamp column to datetime
corpus_df['timestamp'] = pd.to_datetime(corpus_df['timestamp'], unit='s')

# Filter out values not from 2017
corpus_df = corpus_df[corpus_df['timestamp'].dt.year == 2017]

# Save to CSV
corpus_df.to_csv('merged_corpus_2017.csv', index=False)

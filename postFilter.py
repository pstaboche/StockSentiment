import jsonlines
import csv
import json
import re

# Load the stock symbols
stock_symbols = set()
with open('/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/unique_symbols.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stock_symbols.add(row['Symbol'].lower())  # Convert to lowercase for case insensitivity

# Function to check if any stock symbol is in the text
def contains_symbol(text):
    text = text.lower()  # Convert to lowercase for case insensitivity
    for symbol in stock_symbols:
        pattern = r'(\b|\$|\()'+re.escape(symbol)+r'(\b|\)|\])'
        if re.search(pattern, text):
            return True
    return False

# Open the utterances file and a new file for writing
with jsonlines.open('/Users/stevenclark/.convokit/downloads/subreddit-wallstreetbets/utterances.jsonl') as reader, jsonlines.open('filtered_utterances.jsonl', mode='w') as writer:
    for obj in reader:
        # Check if the text of the utterance or its replies contains a stock symbol
        if contains_symbol(obj['text']):
            writer.write(obj)

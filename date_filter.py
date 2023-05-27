import pandas as pd

# Read the CSV file
input_file = '/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/combined_data.csv'
market_data = pd.read_csv(input_file)

# Convert the 'Date' column to a datetime object
market_data['Date'] = pd.to_datetime(market_data['Date'])

# Filter data for dates after March 14, 2008
filtered_data = market_data[market_data['Date'] > '2008-03-14']

# Write the filtered data to a new CSV file
output_file = 'filtered_market_data.csv'
filtered_data.to_csv(output_file, index=False)

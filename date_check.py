import pandas as pd

# Read the filtered CSV file
filtered_data_file = 'filtered_market_data.csv'
filtered_data = pd.read_csv(filtered_data_file)

# Convert the 'Date' column to a datetime object
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

# Find the minimum and maximum dates in the filtered data
min_date = filtered_data['Date'].min()
max_date = filtered_data['Date'].max()

print(f'Date range in the filtered data: {min_date} to {max_date}')

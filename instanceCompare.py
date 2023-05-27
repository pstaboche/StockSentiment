import pandas as pd

# Read symbols.csv
symbols_df = pd.read_csv('symbols.csv')

# Read symbol_counts.csv
symbol_counts_df = pd.read_csv('symbol_counts.csv')

# Find the missing symbols
missing_symbols = set(symbols_df['Symbol']) - set(symbol_counts_df['Symbol'])

# Print the missing symbols
print("Missing symbols:")
print(missing_symbols)

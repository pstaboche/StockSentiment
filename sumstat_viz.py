import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("output_2017.csv")

# Calculate summary statistics for numeric variables
numeric_stats = df.describe()

# Calculate summary statistics for categorical variables
categorical_stats = df.describe(include=['O'])

# Calculate mode for categorical variables
mode = df.mode().dropna()

# Count frequency of the 'Symbol' categorical variable
symbol_counts = df['Symbol'].value_counts()

# Display the number of rows and columns in the dataset
num_rows, num_columns = df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

# Save summary statistics to separate CSV files
numeric_stats.to_csv('numeric_stats.csv')
categorical_stats.to_csv('categorical_stats.csv')
mode.to_csv('mode.csv')
symbol_counts.to_csv('symbol_counts.csv')

# Create a histogram for the 'Daily_Return' variable
plt.hist(df['Daily_Return'])
plt.title('Daily Return Histogram')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.savefig('daily_return_histogram.png')

# Create a box plot for the 'Volume' variable
plt.boxplot(df['Volume'])
plt.title('Volume Box Plot')
plt.ylabel('Volume')
plt.savefig('volume_box_plot.png')

# Create a pivot table between 'Symbol' and 'Daily_Return' (mean)
pivot_table = pd.pivot_table(df, values='Daily_Return', index='Symbol', aggfunc='mean')
pivot_table.to_csv('symbol_daily_return_pivot.csv')

print("Summary statistics, mode, frequency count, and visualizations have been generated and saved.")

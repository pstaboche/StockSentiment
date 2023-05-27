import pandas as pd

def main():
    input_file = '/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/market.US.2017.csv'
    output_file = 'unique_symbols.csv'

    # Read the combined data from the input file
    df = pd.read_csv(input_file)

    # Extract unique symbols and their types
    unique_symbols = df[['Folder', 'Symbol']].drop_duplicates()

    # Save the unique symbols and their types to a new CSV file
    unique_symbols.to_csv(output_file, index=False)
    
    # Generate summary statistics
    summary_stats = unique_symbols['Folder'].value_counts()
    
    print("\nSummary Statistics:")
    print(summary_stats)
    
if __name__ == '__main__':
    main()


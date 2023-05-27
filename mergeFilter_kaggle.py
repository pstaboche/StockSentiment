
import os
import pandas as pd

def main():
    etf_folder = '/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/ETFs'
    stocks_folder = '/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/Stocks'
    output_file = 'market.US.2017.csv'

    combined_data = []

    # Process files in the Stocks folder
    combined_data.extend(process_files_in_folder(stocks_folder, 'Stock'))

    # Process files in the ETF folder
    combined_data.extend(process_files_in_folder(etf_folder, 'ETF'))

    # Create a DataFrame from the combined data
    df = pd.DataFrame(combined_data[1:], columns=combined_data[0])

    # Sort the DataFrame first by 'Folder' (Stock/ETF) and then by 'Symbol' in alphabetical order
    df.sort_values(by=['Folder', 'Symbol'], inplace=True)

    # Save the combined data to a .csv file
    df.to_csv(output_file, index=False)

def process_files_in_folder(folder_path, folder_name):
    data = []

    for file in os.listdir(folder_path):
        if file.endswith('.us.txt'):
            file_path = os.path.join(folder_path, file)

            # Extract the symbol name
            symbol = file[:-7]

            # Read the .txt file contents and add the symbol name
            with open(file_path, 'r') as f:
                lines = f.readlines()

                # Process the header row only once
                if len(data) == 0:
                    header = lines[0].strip().split(',')
                    data.append(['Folder', 'Symbol'] + header)

                for line in lines[1:]:  # Skip the header row
                    # Split the line by comma and add the folder name, symbol, and row data
                    row = line.strip().split(',')
                    
                    # Filter rows with dates from 2017
                    if row[0].startswith('2017'):
                        data.append([folder_name, symbol] + row)

    return data

if __name__ == '__main__':
    main()

import csv
from datetime import datetime

# Function to check if the date is in 2017
def is_date_in_2017(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.year == 2017

# Read the input CSV file
with open('/Users/stevenclark/Academic/UMD_School/Spring 2023/447 Data Manipulation/project/kaggle_cleaned.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    
    # Create the output CSV file
    with open('output_2017.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Write the header row
        header_row = next(csv_reader)
        csv_writer.writerow(header_row)

        # Iterate through rows and write rows with dates in 2017
        for row in csv_reader:
            if is_date_in_2017(row[1]):
                csv_writer.writerow(row)

print("New CSV file 'output_2017.csv' containing only dates from 2017 has been generated.")

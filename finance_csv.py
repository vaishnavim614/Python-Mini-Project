import csv

# Define a dictionary to map bank symbols to their column indices
finance_columns = {'RELIANCE': [2, 3], 'MUTHOOT': [4, 5], 'BAJAJ': [6, 7], 'IIFL':[8,9],'ABSL':[10,11]}

# Create an empty list to hold the transformed data
transformed_data = []

# Read the original CSV data and iterate over its rows
with open('output.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract the date and sector from the current row
        date = row[0]
        sector = row[1]

        # Iterate over the three banks
        for finance, columns in finance_columns.items():
            # Extract the RS and RM values for the current bank
            rs = float(row[columns[0]])
            rm = float(row[columns[1]])

            

            # Append a new row to the transformed data
            transformed_data.append([finance, date, rs, rm, sector])

# Write the transformed data to a new CSV file
with open('FINANCE.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Symbol', 'Date', 'RS', 'RM', 'Sector'])
    writer.writerows(transformed_data)

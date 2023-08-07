import csv

# Define a dictionary to map bank symbols to their column indices
pharma_columns = {'AARTI': [2, 3], 'CIPLA': [4, 5], 'PFIZER': [6, 7], 'SUN':[8,9],'AJANTA':[10,11]}

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
        for pharma, columns in pharma_columns.items():
            # Extract the RS and RM values for the current bank
            rs = float(row[columns[0]])
            rm = float(row[columns[1]])

            

            # Append a new row to the transformed data
            transformed_data.append([pharma, date, rs, rm, sector])

# Write the transformed data to a new CSV file
with open('PHARMA.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Symbol', 'Date', 'RS', 'RM', 'Sector'])
    writer.writerows(transformed_data)

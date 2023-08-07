import csv

bank_columns = {'HDFC': [2, 3], 'ICICI': [4, 5], 'KOTAK': [6, 7], 'AXIS':[8,9],'SBI':[10,11]}

transformed_data = []

with open('output.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        date = row[0]
        sector = row[1]

        
        for bank, columns in bank_columns.items():
            
            rs = float(row[columns[0]])
            rm = float(row[columns[1]])

            transformed_data.append([bank, date, rs, rm, sector])


with open('BANK.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Symbol', 'Date', 'RS', 'RM', 'Sector'])
    writer.writerows(transformed_data)

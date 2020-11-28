import csv

with open('business-price-indexes-june-2020-quarter-corrections-to-previously-published-statistics.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}----->{row[1]}----->{row[2]}---->{row[3]}---->{row[4]}')
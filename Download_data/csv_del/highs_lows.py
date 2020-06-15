import  csv

filename = ''

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

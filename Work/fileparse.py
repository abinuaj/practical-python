# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types =None, has_headers=True):
  
    with open(filename) as f:
        rows = csv.reader(f)


        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:    
                continue
            if indices:
                row = [ row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row) ]  
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

records = parse_csv('Data/portfolio.csv', types=[str, int, float])
print(records)
records = parse_csv('Data/portfolio.csv', types=[str, int, float], select = ['name', 'shares'])
print(records)
records = parse_csv('Data/prices.csv',types =[str, float], has_headers= False)
print(records)
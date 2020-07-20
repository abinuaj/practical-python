# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holdings = {'name':row[0],
             'shares':int(row[1]),
              'price':float(row[2])}
            portfolio.append(holdings)
            
    return portfolio

def read_prices(filename):
    prices ={}

    f = open('Data/prices.csv','r')
    rows =csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
                pass

    return prices    

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost =0.0
current_value =0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']
    current_value += s['shares'] * prices[s['name']]

print('Total cost:', total_cost)
print('Current value:', current_value)
print('Gain/Loss:',current_value -total_cost)
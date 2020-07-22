# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    with open(filename) as filename:
        portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])

    return portfolio

def read_prices(filename):
    with open(filename) as filename:
        prices = parse_csv(filename, has_headers=False, types=[str, float])
        prices = dict(prices)

    return prices   

def make_report(portfolio, prices):
    rows =[]
    for holdings in portfolio:
        current_price = prices[holdings['name']]
        change = current_price - holdings['price']
        summary = (holdings['name'], holdings['shares'], current_price, change)
        rows.append(summary)
    return rows   


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    for r in report:
        print('%10s %10d %10.2f %10.2f' %r) 

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)
    print_report(report)
#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ =='__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python report.py <portfolio.csv> <prices.csv>')
    else:    
        portfolio_report(sys.argv[1], sys.argv[2])
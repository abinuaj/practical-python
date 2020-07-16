# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    '''
with open('Data/portfolio.csv') as file:
    headers = next(file)
    total = 0
    for line in file:
        row = line.split(',')
        no_of_shares = int(row[1])
        price = float(row[2])
        total += no_of_shares * price
print('total_cost_of_shares', total)
    '''
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

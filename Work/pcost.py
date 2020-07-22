import report as rep
def portfolio_cost(filename):
    portfolio = rep.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])


import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
if __name__ == '__main__':
    import sys
    main(sys.argv)


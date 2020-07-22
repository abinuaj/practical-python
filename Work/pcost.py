import report as rep
def portfolio_cost(filename):
    portfolio = rep.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python pcost.py <portfolio.csv> <prices.csv>')
    else:    
        portfolio_report(sys.argv[1], sys.argv[2])


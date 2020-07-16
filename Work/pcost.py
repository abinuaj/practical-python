with open('Data/portfolio.csv') as file:
    headers = next(file)
    total = 0
    for line in file:
        row = line.split(',')
        no_of_shares = int(row[1])
        price = float(row[2])
        total += no_of_shares * price
print('total_price',total)

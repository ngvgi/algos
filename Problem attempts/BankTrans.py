def solution(transactions, dates):
    months = [int(date[5:7]) for date in dates]
    deductible_months = 12
    hash = dict()

    for month in range(len(months)):
        if transactions[month] < 0:
            hash[months[month]] = hash.get(months[month], 0) + abs(
                transactions[month])

    deductible_months -= sum(value >= 100 for value in hash.values())

    balance = sum(transactions) - (deductible_months * 5)
    return balance


transactions = [100, 100, -10, -20, -30]
dates = ['2020-01-01', '2020-02-01', '2020-02-11', '2020-02-05', '2020-02-08']

# transactions = [180, -50, -25, -25]
# dates = ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-31']

# transactions = [100, 100, 100]
# dates = ['2020-12-31', '2020-12-22', '2020-12-03']

ans = solution(transactions, dates)
print(ans)

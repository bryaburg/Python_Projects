stocks = {
    "GOOG" : 520.24,
    "FB" : 76.45,
    "YHOO" : 39.38,
    "AMZN" : 306.21, 
    "AAPL" : 99.76
}

print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))

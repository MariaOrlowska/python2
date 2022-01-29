initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
capital = initialCapital
while year < maxTimeYears:
    year += 1
    capital = round((1+percent)*capital, 2)
    print('After this year:', year, 'you will have:', capital)
else:
    print('The total revenue is', capital-initialCapital)

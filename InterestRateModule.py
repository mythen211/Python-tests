import numpy as np

def interest(days,ccy):
    #Dictionary in absense of market data feed,
    #list represents [o/n, 1mn, 6mn, 12mn]

    interest_rates = {'EUR': [0.05, 0.04, 0.05, 0.05],
                  'USD': [0.06, 0.05, 0.05, 0.05],
                  'GBP': [0.04, 0.045, 0.05, 0.06],
                  'CHF': [0.02, 0.03, 0.03, 0.035]}

    date_marks = [1,30,180,365]
    ccy_rate = interest_rates[ccy]

    if  1 < days < 30:
        y = ccy_rate[0:2]
        x = date_marks[0:2]
    elif 31 < days < 180:
        y = ccy_rate[1:3]
        x = date_marks[1:3]
    else:
        y = ccy_rate[2:4]
        x = date_marks[2:4]

    interpolation = np.interp(days,x,y)

    return interpolation


"""
x = [95, 102.5]
y = [5, 17]

x_new = 100

y_new = np.interp(x_new, x, y)
"""
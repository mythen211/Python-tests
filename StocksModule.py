

def stock_price_ccy(ticker):
    #To update this either with API feed or db feed
    stocks = {'ALV GR': [100.56,'EUR'],
              'BMW GR': [78.09, 'EUR'],
              'MC FP':[230,'EUR'],
              'NOVN SW':[180,'CHF'],
              'ROG SW':[230,'CHF'],
              'AAPL US':[300,'USD']}

    return stocks[ticker]

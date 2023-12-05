import datetime as dt

def expiry(date):
    months  = {'Jan24': dt.datetime(2024, 1, 23),
             'Feb24': dt.datetime(2024,2,20),
             'Mar24':dt.datetime(2024,3,19),
                'Apr24': dt.datetime(2024,4,23),
               'May24': dt.datetime(2024,5,21),
               'Jun24': dt.datetime(2024,6,25),
                'Jul24': dt.datetime(2024, 7, 23),
                'Aug24': dt.datetime(2024,8,20),
                'Sep24': dt.datetime(2024,9,24),
                'Oct24': dt.datetime(2024,10,22),
                'Nov24': dt.datetime(2024,11,19),
                'Dec24': dt.datetime(2024,12,24),
               'Jan25':dt.datetime(2025,1,21)}

    x = months[date] - dt.datetime.now()
    return x.days



'''
x = dt.datetime.now()
print(x.month)
y = x + dt.timedelta(days=17)
print(y.date())
z = dt.datetime(2023, 5,1)

interest = (y-x)
notional = 1000000
ir = 0.05
cal = notional*ir*(interest.days/360)
print(cal)
'''

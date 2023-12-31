import pandas as pd
import datetime

df = pd.read_csv('Men ODI Player Innings Stats - 21st Century.csv', parse_dates=['Innings Date'])
date1 = datetime.datetime(2020, 3, 1)
date2 = datetime.datetime(2021, 1, 1)

filt1 = (df['Innings Batted Flag'] > 0)
df1 = df[filt1]

filt2 = ((df1['Innings Date'] < date2) & (df1['Innings Date'] > date1))
df2 = df1[filt2]
df2['Innings Runs Scored Num'] = df2['Innings Runs Scored Num'].astype(int)

df3 = df2.sort_values(by='Innings Runs Scored Num', ascending=False)
df4 = df3['Innings Player','Innings Runs Scored Num','Innings Date']
df4.to_csv('date filter.csv')


#pivot = pd.pivot_table(df2,values='Innings Runs Scored Num',
 #                     index='Innings Player',
  #                     aggfunc='mean')
#print(pivot)


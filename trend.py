import pytrends
import matplotlib.pyplot as plt
%matplotlib inline
from pytrends.request import TrendReq
from pytrends import dailydata


pytrends = TrendReq(hl='en-US', tz=360)

pytrends.build_payload(["bitcoin"], cat=0, timeframe='today 7-y', geo='US', gprop='')

df1 = pytrends.interest_over_time()

df1.to_csv(index=False)




#other way of doing it day by day and then group up the days by 7 iterval 

df2 = dailydata.get_daily_data('bitcoin', 2015, 1, 2022, 9, geo = 'US')

df2.to_csv(index=False)



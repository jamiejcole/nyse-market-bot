import pandas as pd
import quandl
import datetime
import pylab
import matplotlib.pyplot as plt

start = datetime.datetime(2018,1,1)
end = datetime.date.today()
quandl.ApiConfig.api_key = "_mEXfKTb2sgScinopKpX"
 
# Let's get Apple stock data; Apple's ticker symbol is AAPL - test
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date

data = quandl.get("NASDAQOMX/NQAU60AUD", start_date=start, end_date=end)
type(data)


pylab.rcParams['figure.figsize'] = (15, 9)
data["Index Value"].plot(grid = True)

plt.show()
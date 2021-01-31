import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import quandl
import datetime
import pylab
plt.style.use('bmh')


start = datetime.datetime(2018,1,1)
end = datetime.date.today()
quandl.ApiConfig.api_key = "_mEXfKTb2sgScinopKpX"

df = quandl.get("NASDAQOMX/NQAU60AUD", start_date=start, end_date=end)
type(df)

futureDays = 25
df['Prediction'] = df[['Index Value']].shift(-futureDays)

x = np.array(df.drop(['Prediction'], 1))[:-futureDays]
y = np.array(df['Prediction'])[:-futureDays]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

tree = DecisionTreeRegressor().fit(x_train, y_train)

x_future = df.drop(['Prediction'], 1)[:-futureDays]
x_future = x_future.tail(futureDays) 
x_future = np.array(x_future)


tree_prediction = tree.predict(x_future)


predictions = tree_prediction

valid =  df[x.shape[0]:]
valid['Predictions'] = predictions #Create a new column called 'Predictions' that will hold the predicted prices
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.plot(df[['Index Value']])
plt.plot(valid[['Predictions']], "b-")
plt.legend(['Train', 'Val', 'Prediction' ], loc='lower right')
plt.show()
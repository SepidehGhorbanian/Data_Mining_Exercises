"""

@author: UNISEPP
"""
# Time series Decomposition on air passengers dataset 

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from statsmodels.tsa.seasonal import seasonal_decompose

# preparing the data
df = pd.read_csv('AirPassengers.csv' , parse_dates=['Month'] , index_col=['Month'])
# print(df.head())
df.rename(columns = {'#Passengers' : 'Passengers'} , inplace = True)
print(df.info)
print(df.describe)

# plotting 
fig, ax = plt.subplots()
plt.xlabel('Years')
plt.ylabel('Passengers')
plt.title('Number of passengers by month')
plt.plot (df , color = 'black')
ax.xaxis.set_major_formatter(DateFormatter('%Y'))

# Decomposing
plt.rcParams['figure.figsize'] = [7,8]
sd1 = seasonal_decompose(df , model = 'additive' , period=12)
print(sd1.plot())
sd2 = seasonal_decompose(df , model = 'multiplicative')
print(sd2.plot())
plt.show()

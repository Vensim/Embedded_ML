
#Libraries
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

#Initialisations
series = read_csv('AD8232_data_base.csv', header=0, index_col=0).T
print(series)
dataframe = DataFrame()
dataframe[1] = [series.index[i] for i in range(len(series))]
print(dataframe)
#Time series analysis - Lag features

temps = dataframe
width = 1000
shifted = temps.shift(width - 1)
window = shifted.rolling(window=width)

dataframe = concat([window.min(), window.mean(), window.max(), temps], axis=1)
dataframe.columns = ['min', 'mean', 'max', 't+1']
print(dataframe.head(10000))

dataframe.to_csv('ECG_features', index=False)
		
		
#dataframe_lagged = concat([temp.shift(1), temp], axis=1)
#print(dataframe_lagged)
#dataframe_lagged.columns = ['t-1', 't+1']
#print(dataframe_lagged.head(5))


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


dataframe_lagged = concat([temp.shift(1), temp], axis=1)
print(dataframe_lagged)
dataframe_lagged.columns = ['t-1', 't+1']
print(dataframe_lagged.head(5))

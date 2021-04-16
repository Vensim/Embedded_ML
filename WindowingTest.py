#Libraries
import pandas as pd
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import matplotlib.pyplot as plt
import numpy as np

#Initialisations
series = read_csv('AD8232_data_base.csv', header=0, index_col=0).T
print(series)
dataframe = DataFrame()
dataframe[1] = [series.index[i] for i in range(len(series))]
print(dataframe)



#Time series analysis - Lag features
t = np.arange(0, 5000, 1)

temps = dataframe
width = 1000
shifted = temps.shift(width - 1)
window = shifted.rolling(window=width)
print("Data Frame:")
print(temps)
print("Shifted frame: ")
print(shifted)
print("Window : ")
print(window)

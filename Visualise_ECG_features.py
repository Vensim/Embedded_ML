import pandas as pd
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("ECG_features.csv", delimiter=",", names=["min", "mean", "max", "t"])
print(data)

t = np.arange(0, 10000, 1)
plt.plot(t, data['min'])
plt.plot(t,data['mean'])
plt.plot(t,data['max'])
plt.plot(t,data['t'])
plt.show()

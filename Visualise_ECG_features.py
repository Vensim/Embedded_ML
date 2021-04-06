import pandas as pd
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("ECG_features.csv", delimiter=",", names=["min", "mean", "max", "sensor"])
print(data)

t = np.arange(0, 5000, 1)
plt.plot(t, data['min'], label="min")
plt.plot(t,data['mean'], label="mean")
plt.plot(t,data['max'], label="max")
plt.plot(t,data['sensor'], label="sensor")
plt.legend()
plt.savefig("ECG_feature_extraction.png")
plt.show()

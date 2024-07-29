from tkinter.tix import Y_REGION
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('IPD,OPD.csv')

X = data['OPD'].values
Y = data['IPD'].values


plt.plot(X, Y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Your Data Plot')
# plt.legend)
plt.bar(X,Y)
plt.show()

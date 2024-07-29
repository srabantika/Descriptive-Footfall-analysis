import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('IPDOPD.csv')

IPD = data['IPD'].values
OPD = data['OPD'].values
DATE = data['DATE'].values

plt.plot(DATE, IPD, marker='o')
plt.plot(DATE, OPD, marker='x')
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.legend(['IPD', 'OPD'])

plt.show()

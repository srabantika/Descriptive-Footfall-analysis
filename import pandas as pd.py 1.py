import pandas as pd

import numpy as np

import matplotlib.pyplot as plt 
 
df = pd.read_csv('C:\\Users\\podde\\OneDrive\\Desktop\\hospitalrecordgraph.csv') 

df.plot(x='patiens in outdoor', y= 'admitted' )

plt.xlabel('patient in outdoor, label') 
plt.ylabel('admitted ,label') 
plt.title('hospital graph') 
plt.show()

 
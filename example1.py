import pandas as pd

import matplotlib.pyplot as plot

 

# A python dictionary

data = {"Car Price":[24050, 34850, 38150],

        "Kerb Weight":[3045, 3572, 36380]

        }

index     = ["Variant1", "Variant2", "Variant3"]

 

# Dictionary loaded into a DataFrame       

dataFrame = pd.DataFrame(data=data, index=index)

 

# Draw a vertical bar chart

dataFrame.plot.bar(rot=15, title="Car Price vs Car Weight comparision for Sedans made by a Car Company");

plot.show(block=True)
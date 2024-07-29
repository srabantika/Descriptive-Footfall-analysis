import matplotlib.pyplot as plt

plt.plot(years, apples, marker='o')
plt.plot(years, oranges, marker='x')
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.legend(['Apples', 'Oranges'])

plt.show()
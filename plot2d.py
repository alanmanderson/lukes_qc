import matplotlib.pyplot as plt
import numpy as np
from data import *

fig, ax = plt.subplots()
ax.ticklabel_format(useOffset=False)

plt.scatter(longitude, latitude, marker='.',
            label="Location")
plt.plot(longitude, latitude, '-o')
plt.annotate('parking', xy=(longitude[0], latitude[0]), xytext=(3, 3), color='green' , textcoords='offset points')
plt.annotate('king size candybar', xy=(longitude[6], latitude[6]), xytext=(10, 10), color='blue' , textcoords='offset points')
plt.annotate('facepaint', xy=(longitude[31], latitude[31]), xytext=(10, 10), color='red' , textcoords='offset points')
plt.plot(longitude[0], latitude[0], 'og')
plt.plot(longitude[6], latitude[6], 'ob')
plt.plot(longitude[31], latitude[31], 'or')
plt.margins(x=None, y=None, tight=True)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc='upper left')
plt.show()

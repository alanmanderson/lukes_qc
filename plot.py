import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from data import *

LABEL_SIZE = 10
PARKING = 0
CANDYBAR = 6
FACEPAINT = 31

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.ticklabel_format(useOffset=False)
ax.ticklabel_format(style='', scilimits=None, useOffset=None, axis='both')
ax.plot(longitude, latitude, t, '-o', label='location by time')
ax.text(longitude[PARKING], latitude[PARKING], t[PARKING], "parking", size=LABEL_SIZE, zorder=1, color='g')
ax.text(longitude[CANDYBAR], latitude[CANDYBAR], t[CANDYBAR], "king size candybar", size=LABEL_SIZE, zorder=1, color='g')
ax.text(longitude[FACEPAINT], latitude[FACEPAINT], t[FACEPAINT], "facepaint", size=LABEL_SIZE, zorder=1, color='g')
ax.text(longitude[-1], latitude[-1], t[-1], "parking", size=LABEL_SIZE, zorder=1, color='g')
ax.set_xlabel("\nLongitude")
ax.set_ylabel("\nLatitude")
ax.set_zlabel("\n\nTime")
ax.legend()

for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)

for label in ax.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)

for label in ax.zaxis.get_ticklabels()[::2]:
    label.set_visible(False)

plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:16:46 2021

@author: tamon
"""

import csv
import numpy as np
from scipy.interpolate import griddata
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

speed = []
angles = []
points = []
result = []
sf = []

with open('SpeedAoA.csv', newline='') as csvfile:
    readfile = csv.reader(csvfile, quotechar='|')
    for row in readfile:
        speed.append(row[4])
        angles.append(row[2])
        result.append(row[20])
        sf.append(row[30])

speed.pop(0)
angles.pop(0)
result.pop(0)
sf.pop(0)

speed = [float(i) for i in speed]
angles = [float(i) for i in angles]
for i in range(len(speed)):
    points.append([angles[i], speed[i]])
result = [np.float64(i) for i in result]
sf = [np.float64(j) for j in sf]

xgrid, ygrid = np.mgrid[0:15:1000j, 5:20:1000j]
grid = griddata(points, result, (xgrid, ygrid), method='cubic')
sfs = griddata(points, sf, (xgrid, ygrid), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(angles, speed, 'k.', ms=1)
plt.contour(xgrid, ygrid, sfs, levels=[1])
sp = ax.imshow(grid.T, cmap='jet', extent=(0, 15, 5, 20), origin='lower')
ax.set_aspect(1)
ax.set_xlabel(r'$\alpha$ [deg]')
ax.set_ylabel('Speed [knots]')
clb = fig.colorbar(sp)
clb.set_label('Equivelant Maximum Stress [Pa]')
fig.savefig('speedaoa.pdf', format='pdf', bbox_inches='tight')

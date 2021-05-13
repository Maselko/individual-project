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

radius = []
angles = []
points = []
result = []

with open('angrad.csv', newline='') as csvfile:
    readfile = csv.reader(csvfile, quotechar='|')
    for row in readfile:
        radius.append(row[12])
        angles.append(row[13])
        result.append(row[20])

radius.pop(0)
angles.pop(0)
result.pop(0)
radius = [int(i) for i in radius]
angles = [int(i) for i in angles]
for i in range(len(radius)):
    points.append([angles[i], radius[i]])
result = [np.float64(i) for i in result]

xgrid, ygrid = np.mgrid[10:90:1000j, 30:240:1000j]
grid = griddata(points, result, (xgrid, ygrid), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(angles, radius, 'k.', ms=1)
sp = ax.imshow(grid.T, cmap='jet', extent=(10, 90, 30, 240), origin='lower')
ax.set_aspect(80/(210))
ax.set_xlabel('Angle [deg]')
ax.set_ylabel('Radius [mm]')
clb = fig.colorbar(sp)
clb.set_label('Equivelant Maximum Stress [Pa]')
fig.savefig('angrad.pdf', format='pdf', bbox_inches='tight')
plt.show()

angslice1 = []
angslice2 = []
angslice3 = []
angs = np.linspace(10, 90, 9)
j = 1
for j in range(9):
    angslice1.append(result[8*j + 0])
    angslice2.append(result[8*j + 1])
    angslice3.append(result[8*j + 2])

xnew = np.linspace(10, 90, 200)
f1 = interp1d(angs, angslice1, kind='cubic')
f2 = interp1d(angs, angslice2, kind='cubic')
f3 = interp1d(angs, angslice3, kind='cubic')
plt.plot(xnew, f1(xnew), 'r', label='Radius=30 [mm]')
plt.plot(xnew, f2(xnew), 'b', label='Radius=60 [mm]')
plt.plot(xnew, f3(xnew), 'g', label='Radius=90 [mm]')
plt.grid('major')
plt.legend(loc='lower right')
plt.xlabel('Angle [deg]')
plt.ylabel('Equivelant Maximum Stress [Pa]')
plt.savefig('angslice.pdf', format='pdf', bbox_inches='tight')


# angslice1 = []
# angslice2 = []
# angslice3 = []
# angs = np.linspace(10, 90, 9)
# j = 1
# for j in range(9):
#     angslice1.append(result[8*j + 0])
#     angslice2.append(result[8*j + 1])
#     angslice3.append(result[8*j + 2])

# xnew = np.linspace(10, 90, 200)
# f1 = interp1d(angs, angslice1, kind='cubic')
# f2 = interp1d(angs, angslice2, kind='cubic')
# f3 = interp1d(angs, angslice3, kind='cubic')
# plt.plot(xnew, np.gradient(f1(xnew)), 'r', label='Radius=30 [mm]')
# plt.plot(xnew, np.gradient(f2(xnew)), 'b', label='Radius=60 [mm]')
# plt.plot(xnew, np.gradient(f3(xnew)), 'g', label='Radius=90 [mm]')
# plt.grid('major')
# plt.legend(loc='lower right')
# plt.xlabel('Angle [deg]')
# plt.ylabel('Equivelant Maximum Stress [Pa]')
# plt.savefig('angslice.pdf', format='pdf', bbox_inches='tight')


radslice1 = result[:8]
radslice2 = result[8:16]
radslice3 = result[16:24]
radslice4 = result[24:32]
radslice5 = result[32:40]
radslice6 = result[40:48]
radslice7 = result[48:56]
rads = np.linspace(30, 240, 8)

xnew = np.linspace(30, 240, 200)
f1 = interp1d(rads, radslice1, kind='cubic')
f2 = interp1d(rads, radslice2, kind='cubic')
f3 = interp1d(rads, radslice3, kind='cubic')
f4 = interp1d(rads, radslice4, kind='cubic')
f5 = interp1d(rads, radslice5, kind='cubic')
f6 = interp1d(rads, radslice6, kind='cubic')
f7 = interp1d(rads, radslice7, kind='cubic')

fig2 = plt.figure()
ax2 = plt.subplot(111)
ax2.plot(xnew, f1(xnew), 'r', label='Radius=10 [mm]')
ax2.plot(xnew, f2(xnew), 'b', label='Radius=20 [mm]')
ax2.plot(xnew, f3(xnew), 'g', label='Radius=30 [mm]')
ax2.plot(xnew, f4(xnew), 'y', label='Radius=40 [mm]')
ax2.plot(xnew, f5(xnew), 'orange', label='Radius=50 [mm]')
ax2.plot(xnew, f6(xnew), 'cyan', label='Radius=60 [mm]')
ax2.plot(xnew, f7(xnew), 'purple', label='Radius=70 [mm]')
ax2.grid('major')
chartBox = ax2.get_position()
ax2.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
ax2.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)
ax2.set_xlabel('Radius [mm]')
ax2.set_ylabel('Equivelant Maximum Stress [Pa]')
fig2.savefig('radslice.pdf', format='pdf', bbox_inches='tight')

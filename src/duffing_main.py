# -*- coding: utf-8 -*-
"""
@author: Andy Jeong
"""

import numpy as np
import matplotlib.pylab as plt
from duffing import duffing

r = [0, 0]
delta = 0.1
alpha = -1 
beta = 1
gamma = 0.05
omega = 1.4
mass = 1 # fixed
num_Poincare = 30
h = 0.1

arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
tpoints= arrays["tpoints"]
xpoints = arrays["xpoints"]
vpoints = arrays["vpoints"]
apoints = arrays["apoints"]
poincarex = arrays["poincarex"]
poincarev = arrays["poincarev"]
Fpoints = arrays["Fpoints"]
Ppoints = arrays["Ppoints"]
PEpoints = arrays["PEpoints"]
KEpoints = arrays["KEpoints"]
Epoints = arrays["Epoints"]

plt.plot(tpoints,xpoints,label='x vs. t')
plt.xlabel('Time t [s]')
plt.ylabel('Displacement [x]')
plt.legend()
plt.show()

plt.plot(tpoints,vpoints,label='v vs. t')
plt.ylabel('Velocity v [m/s]')
plt.xlabel('Time t [s]')
plt.legend()
plt.show()

plt.plot(tpoints,apoints,label='a vs. t')
plt.ylabel('Acceleration a [m/s^s]')
plt.xlabel('Time t [s]')
plt.legend()
plt.show()

plt.plot(xpoints,vpoints,label='v vs. x')
plt.xlabel('Displacement x [m]')
plt.ylabel('Velociy v [m/s]')
plt.legend()
plt.show()

plt.scatter(poincarex,poincarev,label='Poincare')
plt.xlabel('Displacement x [m]')
plt.ylabel('Velociy v [m/s]')
plt.legend()
plt.show()

z = np.zeros(len(xpoints))
plt.plot(xpoints[1000:],Ppoints[1000:],label='Potential vs. x',color='b')
plt.plot(xpoints[1000:],Fpoints[1000:],label='F vs. x',color='r')
plt.plot(xpoints, np.zeros(len(xpoints)),'--',linewidth=0.5,color='k')
idx = np.argwhere(np.diff(np.sign(Fpoints - z))).flatten()
for i in range(len(idx)):
    if (np.abs(Fpoints[idx[i]]) < 1e-2):
        plt.plot(xpoints[idx[i]], Fpoints[idx[i]], '*')
plt.xlabel('Displacement x [m]')
plt.ylabel('Force F / Potential V')
plt.legend()
plt.show()

plt.plot(tpoints,KEpoints,label='KE vs. t',color='y')
plt.plot(tpoints,PEpoints,label='PE vs. t',color='b')
plt.plot(tpoints,Epoints,'--',label='Total E vs. t',color='k')
plt.xlabel('Time [s]')
plt.ylabel('Energy [J]')
plt.legend()
plt.show()


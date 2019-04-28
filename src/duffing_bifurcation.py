# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:31:50 2019

@author: jong7
"""
import numpy as np
import matplotlib.pylab as plt
from duffing import duffing

# get bifurcations
# plots min and max displacement over time to see overall divergence
r = [0, 0]
delta = 0.01
alpha = 1 
beta = 1
#gamma = 1
omega =  1.414
mass = 1 # fixed
num_Poincare = 30
h = 0.01 # kept to 0.1 for running time issue

xmax, xmin = [], []
gammas = np.arange(0, 0.6, h)
for gamma in gammas:
    arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
    xpoints = arrays["xpoints"]
    xmax.append(max(xpoints))
    xmin.append(min(xpoints))
maxlines = plt.scatter(gammas/delta, xmax, label='Max Displacement',color='b',s=10)
minlines = plt.scatter(gammas/delta, xmin, label='Min Displacement',color='r',s=10)
#plt.setp(maxlines, s=0.7)
#plt.setp(minlines, s=0.7)
plt.xlim([20, 40])
plt.ylabel('Displacement')
plt.xlabel('Excitation/Damping Ratio')
plt.title('Bifurcation Diagram')
plt.legend()
plt.show()
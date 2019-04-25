# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:30:20 2019

@author: jong7
"""
import numpy as np
import matplotlib.pylab as plt
from duffing import duffing

# get frequency response
r = [0, 0]
delta = 0.1
alpha = 1 # positive -> negative, negative -> positive
beta = 0.004
gamma = 1
omega =  1.414
mass = 1 # fixed
num_Poincare = 30
h = 0.1

responselist = []
freqlist = []
omegas = np.arange(h,2,h/10)

for omega in omegas:
    arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
    xpoints = arrays["xpoints"]
    response = np.sqrt( 1/( (omega**2 - alpha - 3/4*beta*np.max(xpoints)**2)**2 + (delta*omega)**2 ) )
    responselist.append(response)
    freq = omega/np.sqrt(alpha)
    freqlist.append(freq)

plt.scatter(freqlist, responselist)
plt.xlabel('freq')
plt.ylabel('|X(w)|')
plt.show()

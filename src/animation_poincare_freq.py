# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:51:05 2019
@author: Andy Jeong
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from duffing import duffing
import numpy as np
# Camera reference: https://github.com/jwkvam/celluloid
from celluloid import Camera

# get phase-space diagram
#r = [0,0]
#delta = 0.1
#alpha = -1 
#beta = 1
#gamma = 0.38
#omega = 1.4
#mass = 1 # fixed
#num_Poincare = 20
#h = 0.1 # kept to 0.1 for running time issue
#
#arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
#xpoints = arrays["xpoints"]
#ypoints = arrays["vpoints"]
#
#ax = plt.figure()
#camera = Camera(ax)
#plt.show()
#for i in range(len(xpoints)):
#    plt.scatter(xpoints, ypoints,color='green',s=10)
#    plt.scatter(xpoints[i], ypoints[i], color='blue',s=30)
#    camera.snap()
#anim = camera.animate(blit=False)
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=100)
#anim.save('scatter.mp4', writer=writer)

# get frequency response
r = [0, 0]
delta = 0.1
alpha = 1 
beta = 0.004
gamma = 1
omega =  1.414
mass = 1 # fixed
num_Poincare = 10
h = 0.1 # kept to 0.1 for running time issue

responselist = []
freqlist = []

# left to right
omegas = np.arange(h,2,h/10)
for omega in omegas:
    arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
    xpoints = arrays["xpoints"]
    response = np.sqrt( 1/( (omega**2 - alpha - 3/4*beta*np.max(xpoints)**2)**2 + (delta*omega)**2 ) )
    responselist.append(response)
    freq = omega/np.sqrt(alpha)
    freqlist.append(freq)

# right to left
omegas = np.arange(2,h,-h/10)
for omega in omegas:
    arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
    xpoints = arrays["xpoints"]
    response = np.sqrt( 1/( (omega**2 - alpha - 3/4*beta*np.max(xpoints)**2)**2 + (delta*omega)**2 ) )
    responselist.append(response)
    freq = omega/np.sqrt(alpha)
    freqlist.append(freq)
    
ax = plt.figure()
camera = Camera(ax)
for i in range(len(freqlist)):
    plt.scatter(freqlist, responselist,color='green',s=0.1)
    plt.scatter(freqlist[i], responselist[i], color='blue',s=10)
    camera.snap()
anim = camera.animate(blit=False)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=500)
anim.save('scatter.mp4', writer=writer)
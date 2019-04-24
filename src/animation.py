# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:17:02 2019
@author: Andy Jeong
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from duffing import duffing

r = [0, 0]
delta = 0.1
alpha = -1 # positive -> negative, negative -> positive
beta = 1
gamma = 0.05
omega = 1.4
mass = 1 # fixed
num_Poincare = 30
h = 0.1

arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
xpoints = arrays["xpoints"]
Ppoints = arrays["Ppoints"]

# Potential vs x
# setup figure, axis, and elements to plot
fig = plt.figure()
ax2 = fig.add_subplot(111, autoscale_on=False, xlim=(np.min(xpoints), np.max(xpoints)), ylim=(np.min(Ppoints), np.max(Ppoints)))
ax2.set_aspect('equal')
ax2.set_xlabel('x')
ax2.set_ylabel('v')
ax2.grid()
line, = ax2.plot([], [], 'bo', lw=1)
# time display
time_template = 'time = %.1fs'
time_text = ax2.text(0.05, 1.03, '', transform=ax2.transAxes)

# plot background of each frame
def init():
    line.set_data([], [])
    time_text.set_text('')
    return time_text

# sequential calls
def animate(i):
    if (xpoints[i]):
        x1 = xpoints[i]
        P1 = Ppoints[i]
        line.set_data(x1,P1)
        time_text.set_text(time_template % (i*h))
        i += 1
    return time_text

ax2.plot(xpoints[np.arange(0,len(xpoints))],
                 Ppoints[np.arange(0,len(Ppoints))],'g-')
ani = animation.FuncAnimation(fig, animate, frames=np.arange(1, len(Ppoints)),
                              interval=0.1, blit=False, init_func=init)
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("myfile.mp4", writer=writer)
plt.show()
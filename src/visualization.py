# -*- coding: utf-8 -*-
"""
@author: Andy Jeong
"""
# visualization through VPython

import numpy as np
from visual import *
from duffing import duffing # custom function
from PIL import ImageGrab   # PIL
from subprocess import call # for issuing commands

r = [0, 0]
delta = 0.1
alpha = -1 # positive -> negative, negative -> positive
beta = 1
gamma = 0.38
omega = 1.4
mass = 1 # fixed
num_Poincare = 100
h = 0.1

arrays = duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h)
xpoints = arrays["xpoints"]

def canvas(scene):  # return canvas bounding box, excluding frames
    return (11,150,515,500)

### for animation
scene = display(title='Chaotic Motion in Moonbeam - simplified')
ceiling = box(pos=(0,0.1,0), size=(4,0.1,1), color=color.yellow)
side = box(pos=(-np.max(xpoints)-0.5,-0.5,0), size=(0.1,1.3,1), color=color.yellow)
floor = box(pos=(0,-1.1,0), size=(4,0.1,1), color=color.green)

# boxes indicate locations for magnets for now
magnet1 = box(pos=(np.max(xpoints),-0.8,0), height=0.5, width=0.5, length=0.5)
magnet2 = box(pos=(-np.max(xpoints),-0.8,0), height=0.5, width=0.5, length=0.5)

fixball = sphere(make_trail = True, trail_type="curve", interval=1, retain=20)
moveball = sphere(make_trail=True, trail_type="curve", interval=1, retain=30, color=color.blue)
fixball.radius=0.1
fixball.pos = (0, 0, 0)
moveball.radius = 0.1
moveball.trail_object.color = color.blue
moveball.pos = (xpoints[0], -1, 0)
pointer = curve(pos=(0,0,0), radius=0.08)

n = 500
# counter, file number
ic, fnum = 0, 0

for i in range(len(xpoints)):
    rate(120)
    moveball.pos = (xpoints[i], -1, 0)
    # obtain a curved structure by approx movement in percentage
    # curve() only follows along an axis, so it's hard to achieve
    # a dynamically moving structure
    pointer.pos=[(0,0,0), \
                 (moveball.x*0.1,moveball.y*0.15,0), \
                 (moveball.x*0.15,moveball.y*0.22,0), \
                 (moveball.x*0.2,moveball.y*0.28,0), \
                 (moveball.x*0.25,moveball.y*0.35,0), \
                 (moveball.x*0.4,moveball.y*0.53,0),  \
                 (moveball.x*0.6,moveball.y*0.74,0),  \
                 (moveball.x*0.7,moveball.y*0.85,0), \
                 (moveball.x*0.8,moveball.y*0.92,0), \
                 (moveball.x*0.9,moveball.y*0.99,0), \
                 (moveball.x,moveball.y,0)]
    # trail for previous 4 points
    pointer.retain = 4
    
    # capture images
    if (fnum >= len(xpoints)):
        break
    elif (ic%20 == 0):      # grab every 20 iterations, may need adjustment
        im = ImageGrab.grab(canvas(scene))
        num = '00'+repr(fnum)           # sequence num 000-00999, trunc. below
        im.save('img-'+num[-3:]+'.png') # save to png file, 000-999, 3 digits
        fnum += 1
    ic += 1
    
# if the program cannot find "ffmpeg", check its path. can also replace it with "movie.bat"
call("ffmpeg -r 10 -i img-%3d.png -vcodec libx264 -vf format=yuv420p,scale=412:412 -y movie.mp4")
print ("\n Movie created: movie.mp4")

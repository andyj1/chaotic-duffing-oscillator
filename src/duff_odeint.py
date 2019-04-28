# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:14:20 2019
@author: Andy Jeong
"""

# reference: https://galileo-unbound.blog/2019/03/20/georg-duffing-and-his-equation/
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt

# numerical method to solve Duffing Equation 
# using built-in odeint in scipy.integrate package
# this uses conventional LSODA method, for integrating 1st order diffEq
plt.close('all')
alpha = -1
beta = 1
gamma = 0.05
delta = 0
w = 1.4

def duff(r, t):
    x, v, z = r
    fx = v
    fv = gamma*np.cos(w*t) - alpha*x - beta*x**3 - delta*v
    ftheta = w
    return[fx,fv,ftheta]
                

# initial conditions
#x, v, theta
r = [0, 0, 1.4]

# perform 1st integration twice (odeint)
T = 2*np.pi/w
t1 = np.linspace(0, 2000, 40000)
x1 = integrate.odeint(duff, r, t1)
x0 = x1[len(x1)-1,:]

num = 400000
t2 = np.linspace(1,20000,num)
x2 = integrate.odeint(duff, x0, t2)

xs = x2[:,0]
vs = x2[:,1]
    
plt.figure()

# chaotic
lines1 = plt.plot(xs[1:2000],vs[1:2000],'ko-',ms=1, label='Chaos (initial)')

# transient
lines2 = plt.plot(xs[int(num*0.8):num],vs[int(num*0.8):num],'b-',ms=1, label='Transient')
plt.xlabel('x')
plt.ylabel('v')
plt.title('phase-portrait diagram')
plt.setp(lines1, linewidth=0.5)
plt.setp(lines2, linewidth=2)
plt.legend()
plt.show()

#plt.savefig('Duffing')

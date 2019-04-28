# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 01:01:39 2019

@author: jong7
"""

# main program that computes numerical approximation to the Duffing Equation using Runge-Kutta fourth order method
import numpy as np

"""
* parameters for Duffing Equation
    acceleration + delta*velocity + alpha*x + beta*x^3 = gamma*cos(omega*t)
    
    delta: damping coefficient
    alpha: linear stiffness coefficient
    beta: nonlinearity in the resotring force (if 0, simple harmonic oscillator)
    gamma: amplitude of the driving force
    omega = angular frequency of the driving force
    h: step size for RK4
"""

def duffing(r, delta, alpha, beta, gamma, omega, mass, num_Poincare, h):
    
    # define function
    def f(r, t):
        x = r[0]
        v = r[1]
        fx = v
        fv = -delta*v - alpha*x - beta*x**3 + gamma*np.cos(omega*t)
        return np.array([fx,fv],float)
    
    # define time range
    T = 2*np.pi/omega
    t1, t2 = 0, T*num_Poincare

    # initialize arrays
    tpoints = np.arange(t1, t2, h)
    xpoints, vpoints, apoints, poincarex, poincarev = [], [], [], [], []
    Fpoints, PEpoints, KEpoints, Epoints, Ppoints = [], [], [], [], []
    
    r = np.array(r,float)
    for t in tpoints:    
        x = r[0]
        v = r[1]
        xpoints.append(x)
        vpoints.append(v)
        fv = -delta*v - alpha*x - beta*x**3 + gamma*np.cos(omega*t)
        apoints.append(fv)
        
        # Energy Calculation
        # conservative Force = m*a = a for m =1
        # PE = -integral (Fconsevative) dx
        F = mass*fv
        PE = mass * ( delta*v*x + alpha/2 * x**2 + beta/4 * x**4 - gamma*x*np.cos(omega*t) )
        P = PE/mass
        KE = 1/2 * mass * v**2
        E = KE+PE
        Fpoints.append(F)
        PEpoints.append(PE)
        Ppoints.append(P)
        KEpoints.append(KE)
        Epoints.append(E)
        
        if (t%T) < h:
            poincarex.append(r[0])
            poincarev.append(r[1])
            
        # error ratio calculation for RK4
#        if (t == 0.1):
#            print(t, r[0])
        # RK4
        k1 = f(r,t)
        k2 = f(r+h/2*k1, t+h/2)
        k3 = f(r+h/2*k2, t+h/2)
        k4 = f(r+h*k3,t+h)
        r += h/6*(k1+2*k2+2*k3+k4)
    
    # conversion to numpy array
    xpoints = np.array(xpoints)
    vpoints = np.array(vpoints)
    apoints = np.array(apoints)
    poincarex = np.array(poincarex)
    poincarev = np.array(poincarev)
    Fpoints = np.array(Fpoints)
    Ppoints = np.array(Ppoints)
    PEpoints = np.array(PEpoints)
    KEpoints = np.array(KEpoints)
    Epoints = np.array(Epoints)
    
    # return dictionary of arrays
    return {
        "tpoints" : tpoints , "xpoints" : xpoints, "vpoints" : vpoints,
        "apoints" : apoints, "Fpoints": Fpoints, "Ppoints" : Ppoints,
        "PEpoints" : PEpoints, "KEpoints" : KEpoints, "Epoints": Epoints,
        "poincarex" : poincarex, "poincarev" : poincarev 
        }


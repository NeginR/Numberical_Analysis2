from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from matplotlib import rcParams
from mpmath import chebyt, chop, taylor


def runge(x):
    return 1/(1 +25*x**2)

def rungeee():
    xf= np.linspace(-1,1)
    yf= runge(xf)
    plt.plot(xf,yf,color = "r",label="runge(x)")

def drawChebyshevByPoint(n,clr):
    
    checbyshev = np.polynomial.chebyshev.Chebyshev.interpolate(runge,n,[-1,1])
    xcheby = checbyshev.linspace(n=500,domain=[-1,1])[0]
    ycheby = checbyshev.linspace(n=500,domain=[-1,1])[1]
    plt.plot(xcheby,ycheby,color =clr,label = "chebychecv {}".format(n-1))


rungeee()

a=[6,11,16,21]
b=['gold', 'g', 'c', 'm']
j=0
for i in a:
    drawChebyshevByPoint(i,b[j])
    j+=1

plt.show()

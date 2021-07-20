from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 18

def runge(x):
    return 1/(1 +x**2)

plt.figure(figsize=(8,8))
npts = 301

#line
xpoints =[-5 , 5]
ypoints = [0 , 0]
plt.plot(xpoints,ypoints,  color= 'k')

# Runge Function
x_vec = np.linspace(-5, 5, npts)
y_vec = runge(x_vec)
plt.plot(x_vec, y_vec, lw=2, color='r')

# Fifth degree polynomial
pts_x = np.linspace(-5, 5, 6)
pts_y = runge(pts_x)
poly = lagrange(pts_x, pts_y)
y_interp = poly(x_vec)
plt.plot(x_vec, y_interp, lw=2, color='b')

# Ten degree polynomial
pts_x = np.linspace(-5, 5, 11)
pts_y = runge(pts_x)
poly = lagrange(pts_x, pts_y)
y_interp = poly(x_vec)
plt.plot(x_vec, y_interp, lw=2, color='g') 

# Fifteen degree polynomial
pts_x = np.linspace(-5, 5, 16)
pts_y = runge(pts_x)
poly = lagrange(pts_x, pts_y)
y_interp = poly(x_vec)
plt.plot(x_vec, y_interp, lw=2, color='purple') 

# tweenty degree polynomial
pts_x = np.linspace(-5, 5, 21)
pts_y = runge(pts_x)
poly = lagrange(pts_x, pts_y)
y_interp = poly(x_vec)
plt.plot(x_vec, y_interp, lw=2, color='pink') 



plt.show()
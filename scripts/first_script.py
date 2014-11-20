from numpy import *
from matplotlib import pyplot as plt

xvar = array([1,2,3,4,5])
yvar = xvar*2

plt.clf()
plt.plot(xvar,yvar,'ko')

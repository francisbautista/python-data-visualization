import sys
from numpy import *
from matplotlib import pyplot as plt

#xvar = array([1,2,3,4,5])
#yvar = xvar*2

xvar, yvar = loadtxt("../data/data.csv", unpack=True, delimiter=',')

plt.clf()
plt.plot(xvar,yvar,'rx')
plt.plot(xvar,yvar,'b')

plt.xlim((0,6))
plt.ylim((0,12))

plt.xlabel("My X Variable")
plt.ylabel("My Y Variable")
plt.title("My First Python Plot")
plt.savefig("../fig/fig_first_plot.png")
plt.show()

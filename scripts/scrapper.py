import sys
from numpy import *
from matplotlib import pyplot as plt

fn="../data/data_provinces.csv"

name=loadtxt(fn, unpack=True, delimiter=',', skiprows=1, dtype='a',
usecols=arange(1))

region=loadtxt(fn, unpack=True, delimiter=',', skiprows=1, dtype='a',
usecols=arange(1)+1)

population,lifeExpectancy,incomePerCapita,expenditurePerCapita=loadtxt(fn,unpack=True, delimiter=',', skiprows=1,usecols=arange(4)+2)

region_list=unique(region)
color_list=array(['r', 'b', 'r', 'c', 'r','g','b','b','r','b','g','c','r','b','c','b','r'])
colors=zeros(len(name), dtype='a')

for i in arange(len(name)):
    colors[i]=color_list[region_list==region[i]][0]

plt.clf()
plt.scatter(incomePerCapita,lifeExpectancy, s=population/min(population)*20, c=colors, alpha=0.5)
# plt.xscale(2)
plt.show()


# Main
if __name__ == '__main__':
    main()

## experimental
# N=50
# colors = random.rand(N)
# area = pi * (15 * random.rand(50))**2 # 0 to 15 point radiuses
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

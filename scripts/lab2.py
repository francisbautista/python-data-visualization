import sys, collections
from numpy import *
from matplotlib import pyplot as plt

fn="../data/data_provinces.csv"
# loading file with 3 columns
name=loadtxt(fn, unpack=True, delimiter=',', skiprows=1, dtype='a', usecols=arange(1))
# array defined for the first column
region=loadtxt(fn, unpack=True, delimiter=',', skiprows=1, dtype='a', usecols=arange(1)+1)
# array defined  for the second column
population,lifeExpectancy,incomePerCapita,expenditurePerCapita=loadtxt(fn,unpack=True, delimiter=',', skiprows=1,usecols=arange(4)+2) # array defined for the remaining columns

def main():
    region_list = unique(region)
    population_dict = {}
    for i in range(len(region_list)):
        population_dict[region_list[i]] = popCounter(region_list[i])
    sort_dict = collections.OrderedDict(sorted(population_dict.items()))
    for key in sort_dict:
        print "%s: %s" % (key, sort_dict[key])
    graph(sort_dict)
    sys.exit(1)

# Iterates through each row with the same Region
# and adds population to sum and returns sum value
def popCounter(region_val):
    sum = 0
    reg_index = where(region==region_val)
    for i in range(0,len(reg_index[0])):
        sum = sum + population[reg_index[0][i]]
    return sum

# Set x and y labels and values for barplot
# and then graph values and save in fig folder
def graph(sort_dict):
    plt.bar(range(len(sort_dict)), sort_dict.values(), width=1)
    plt.xticks(range(len(sort_dict)), sort_dict.keys(), rotation=45, size='small')
    plt.ylim((0,15000000))
    plt.xlabel("Population")
    plt.ylabel("Regions")
    plt.title("Regional Populations of the Philippines")
    plt.savefig("../fig/Regional Population.png")
    plt.show()

if __name__ == '__main__':
	main()

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
    age_dict = {}
    for i in range(len(region_list)):
        age_dict[region_list[i]] = ageCounter(region_list[i])
    sort_dict = collections.OrderedDict(sorted(age_dict.items()))
    for key in sort_dict:
        print "%s: %s" % (key, sort_dict[key])
    graph(sort_dict)
    sys.exit(1)

# Iterates through each row with the same Region
# and adds age to sum and returns sum value
def ageCounter(region_val):
    sum = 0
    reg_index = where(region==region_val)
    for i in range(0,len(reg_index[0])):
        sum = sum + (lifeExpectancy[reg_index[0][i]] * population[reg_index[0][i]])
    avg = sum/popCounter(region_val)
    return avg

def popCounter(region_val):
    sum = 0
    reg_index = where(region==region_val)
    for i in range(0,len(reg_index[0])):
        sum = sum + population[reg_index[0][i]]
    return sum

# Set x and y labels and values for barplot
# and then graph values and save in fig folder
def graph(sort_dict):
    plt.yticks(range(len(sort_dict)), sorted(sort_dict.keys(), key=sort_dict.get), rotation=45, size='small')
    plt.barh(range(len(sort_dict)), sorted(sort_dict.values()))
    plt.xlim((0,100))
    plt.xlabel("Life Expectancy")
    plt.ylabel("Regions")
    plt.title("Regional Average Life Expectancy of the Philippines")
    plt.savefig("../fig/Life Expectancy.png")
    plt.show()

if __name__ == '__main__':
	main()

import random
import numpy
import math
import copy
import sys
import matplotlib.pyplot as plt
infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
legend = list()
city = list()
for line in infile:
    legend = legend + line.split() # legend[0]:city legend[1]:x legend[2]:y
m = int(len(legend)/3)
shape = (m,2)
harita = numpy.zeros(shape)
for i in range(len(legend)):
    index = int(i/3)
    if(i%3 is 0):
        harita[index][0] = legend[i]
    elif(i%3 is 1):
        harita[index][0] = legend[i]
    else:
        harita[index][1] = legend[i]
cities = harita
print cities
tour = random.sample(range(len(harita)), len(harita))
print tour
for temperature in numpy.logspace(0, 5, num=100000)[::-1]:
	[i, j] = sorted(random.sample(range(len(harita)), 2))
	newTour = tour[:i] + tour[j:j+1] + tour[i+1:j] + tour[i:i+1] + tour[j+1:]
	if math.exp((sum([math.sqrt(sum([(cities[tour[(k+1) % len(harita)]][d] - cities[tour[k % len(harita)]][d])**2 for d in [0, 1]])) for k in [j, j-1, i, i-1]]) - sum([math.sqrt(sum([(cities[newTour[(k+1) % len(harita)]][d] - cities[newTour[k % len(harita)]][d])**2 for d in [0, 1]])) for k in [j, j-1, i, i-1]])) / temperature) > random.random():
		tour = copy.copy(newTour)
plt.plot(zip(*[cities[tour[i % len(harita)]] for i in range(len(harita)+1)])[0],
         zip(*[cities[tour[i % len(harita)]] for i in range(len(harita)+1)])[1], 'xb-', )
plt.show()
outfile.close()
infile.close()
import numpy
infile = open('example-input-1.txt', 'r')
outfile = open('output.txt', 'w')
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

outfile.write(str(harita))
outfile.close()
infile.close()
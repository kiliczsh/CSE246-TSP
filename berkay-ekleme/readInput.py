import numpy

class Converter:
    def __init__(self,infile,mapfile,outfile):
        self.infile = open(infile, 'r') #open('example-input-1.txt', 'r')
        self.mapfile = open(mapfile, 'w+') #open('output.txt', 'w')
        self.outfile = open(outfile, 'w+') #open('output.txt', 'w')

    def read_and_convert(self):
        legend = list()
        city = list()
        for line in self.infile:
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
            print(str(legend[i]),"read")
        self.mapfile.write(str(harita))
        return harita
    def save_output(self,lnt_path,output):
        self.outfile.write(str(int(round(lnt_path)))+"\n")
        lnt=len(output)
        for i in range(0,lnt-1):
            self.outfile.write(str(output[i])+"\n")
    def finish(self):
        self.outfile.close()
        self.mapfile.close()
        self.infile.close()
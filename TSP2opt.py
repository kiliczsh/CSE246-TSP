from sys import argv
from random import randrange
from city import City
from two_opt import Two_opt

def read_input(filename):
	dimension = sum(1 for line in open(filename))
	inputfile = open(filename, 'r')
	route = []
	# read lines into coordinate system
	for line in inputfile:
		xy = get_xy(line)
		route.append(City(xy))
	inputfile.close()
	# route is a <list>
	return route
	
def write_output(path, filename, firstpoint):
	outfile = open(argv[2], 'w')
	outfile.write(str(int(calc_dist(path)))+"\n")
	for city in path:
		outfile.write(str(city.id)+"\n")
		print(city.id)
	print("Total Cost : " + str(calc_dist(path)))

def calc_dist(path):
    	cost = 0
    	prev_city = path[-1]
    	for city in path:
    		cost += city.calc_formula(prev_city) 
    		prev_city = city
    	return cost

def get_xy(line):
	point = line.split()
	xy = (int(point[0]), int(point[1]), int(point[2]))
	return xy

def main():

	path = read_input(argv[1])

	solver=Two_opt(path)

	first = path[0]

	route = solver.execute()

	

	write_output(route, argv[1], first)

if __name__ == "__main__":
	main()

from sys import argv
from random import randrange
from city import City

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

def get_xy(line):
	point = line.split()
	xy = (int(point[0]), int(point[1]), int(point[2]))
	return xy

def calc_dist(route):
	cost = 0
	prev_city = route[-1]
	for city in route:
		cost += city.calc_formula(prev_city) 
		prev_city = city
	return cost

def swap_2opt(route, i, k):
	"""
	swaps the endpoints of two edges by reversing a section of nodes, 
		ideally to eliminate crossovers
	returns the new route created with a the 2-opt swap
	route - route to apply 2-opt
	i - start index of the portion of the route to be reversed
	k - index of last node in portion of route to be reversed
	pre: 0 <= i < (len(route) - 1) and i < k < len(route)
	post: length of the new route must match length of the given route 
	"""
	new_route = route[0:i]
	new_route.extend(reversed(route[i:k + 1])) #new_route'u tersiyle extend ediyor
	new_route.extend(route[k+1:])

	return new_route

def run_2opt(route):
	"""
	improves an existing route using the 2-opt swap until no improved route is found
	best path found will differ depending of the start node of the list of nodes
		representing the input tour
	returns the best path found
	route - route to improve
	"""
	flag = True
	best_route = route
	best_distance = calc_dist(route)
	while flag:
		flag = False
		for i in range(len(best_route) - 1):
			for k in range(i+1, len(best_route)):
				new_route = swap_2opt(best_route, i, k)
				new_distance = calc_dist(new_route)
				print("\n"+str(new_distance)+"\n\n")
				if new_distance < best_distance:
					best_distance = new_distance
					best_route = new_route
					flag = True
					break  # improvement found, return to the top of the while loop
			if flag:
				break
	assert len(best_route) == len(route)
	return best_route

def write_output(route, filename, firstpoint):
	outfile = open(argv[2], 'w')
	outfile.write(str(int(calc_dist(route)))+"\n")
	for city in route:
		outfile.write(str(city.id)+"\n")
		print(city.id)
	print("Total Cost : " + str(calc_dist(route)))

def main():
	route = read_input(argv[1])
	first_point = route[0]
	route = run_2opt(route)
	write_output(route, argv[1], first_point)

if __name__ == "__main__":
	main()

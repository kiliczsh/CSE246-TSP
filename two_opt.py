class Two_opt:
    
    def __init__(self,path):
        self.path=path

    def calc_dist(self,path):
    	cost = 0
    	prev_city = path[-1]
    	for city in path:
    		cost += city.calc_formula(prev_city) 
    		prev_city = city
    	return cost
		
    def swap(self,i, k):
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
	    tmp = self.path[0:i]
	    tmp.extend(reversed(self.path[i:k + 1])) #new_route'u tersiyle extend ediyor
	    tmp.extend(self.path[k+1:])

	    return tmp

    def execute(self):
	    """
	    improves an existing route using the 2-opt swap until no improved route is found
	    best path found will differ depending of the start node of the list of nodes
	    	representing the input tour
	    returns the best path found
	    route - route to improve
	    """
	    flag = True
	    opt_cost = self.calc_dist(self.path)
    
	    while flag:
	    	print(""+str(opt_cost)+" ")
	    	flag = False
	    	for i in range(len(self.path) - 1):
	    		for k in range(i+1, len(self.path)):
	    			tmp = self.swap(i, k)
	    			tmp_cost = self.calc_dist(tmp)
	    			if tmp_cost < opt_cost:
	    				opt_cost = tmp_cost
	    				self.path = tmp
	    				flag = True
	    				break  # improvement found, return to the top of the while loop
	    		if flag:
	    			break
	    return self.path
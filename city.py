from math import sqrt
class City:
	def __init__(self, coords):
		self.id = coords[0]  # start position in a route's order
		self.x = coords[1]   # x coordinate
		self.y = coords[2]   # y coordinate

	def calc_formula(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return int(round(sqrt(dx*dx + dy*dy)))

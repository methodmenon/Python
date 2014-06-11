class Wheels:
	#w_type = [type1, type2, type3]
	def __init__(self, name, weight, production_cost):
		self.name = name
		self.weight = weight
		self.production_cost = production_cost

class Frames:
	#f_type = [aluminum, carbon, steel]
	def __init__(self, weight, production_cost, f_type):
		self.weight = weight
		self.production_cost = production_cost
		self.f_type = f_type

class Bicycle_Model:
	def __init__(self, name, manufacturer, wheel, frame):
		self.name = name
		self.manufacturer = manufacturer
		self.wheel = wheel
		self.frame = frame

	def total_weight(self):
		total_weight = (self.frame.weight) + (2 * self.wheel.weight)
		return total_weight

	def total_cost(self):
		total_cost = (self.frame.production_cost) + (2 * self.wheel.production_cost)
		return total_cost
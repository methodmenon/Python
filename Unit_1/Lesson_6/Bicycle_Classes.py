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

class Manufacturers:
	def __init__(self, name, model, markup_percentage):
		self.name = name
		self.model = model
		self.markup_percentage = markup_percentage

	def markup_cost(self):
		markup_percentage = (self.markup_percentage/100.0)
		markup_cost = self.model.total_cost * (1 + markup_percentage)
		print markup_cost


class Bike_Shops:
	inventory = {}
	sold = {}
	def __init__(self, name, manufacturer1, manufacturer2, inventory):
		self.name = name
		self.manufacturer1 = manufacturer1
		self.manufacturer2 = manufacturer2
		self.inventory = inventory

	def profit_per_sale(self, markup):
		markup = (1 + (self.markup/100.0))
		profit = (self.markup)*(self.manufacturer.markup_cost) - (self.manufacturer.markup_cost)

	def inventory_change(self, model):
		if self.inventory[model] > 0:
			self.sold[model] += 1
			self.inventory[model] -= 1
		else:
			print("Item not available")

	def total_profit(self):
		profit = 0
		for model in self.sold.keys():
			profit += 





	




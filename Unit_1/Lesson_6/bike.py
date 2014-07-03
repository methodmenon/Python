class Wheels(object):
    #w_type = [type1, type2, type3]
	def __init__(self, name, weight, production_cost):
		self.name = name
		self.weight = weight
		self.production_cost = production_cost

class Frame(object):
	#f_type = [aluminum, carbon, steel]
	def __init__(self, f_type, weight, production_cost):
		self.f_type = f_type
		self.weight = weight
		self.production_cost = production_cost

class Manufacturer(object):
	def __init__(self, name, markup):
		self.markup = (1 + (markup/100.0))

class Bicycle_Model(object):
	def __init__(self, name, wheel, frame, manufacturer):
		self.name = name
		self.manufacturer = manufacturer
		self.wheel = wheel
		self.frame = frame

	def total_weight(self):
		total_weight = (self.frame.weight) + (2 * self.wheel.weight)
		return total_weight

	def total_cost(self):
		self.frame.production_cost = (self.frame.production_cost) * (self.manufacturer.markup)
		self.wheel.production_cost = (self.wheel.production_cost) * (self.manufacturer.markup)
		total_cost = (self.frame.production_cost) + (2 * self.wheel.production_cost)
		return total_cost
		
class Bike_Shop(object):
	inventory = []
	sold_bikes = []
	def __init__(self, name, margin):
		self.name = name
		self.margin = (1 + (margin/100.0))

	def initial_inventory(self):
		for bike in self.inventory:
			print("bike model {}".format(bike.name))

	def show_inventory(self):
		for bike in self.inventory:
			print("bike model: {}, {}".format(bike.name, bike.total_weight()))

##not part of 6/22 check##########################
	def bike_sale_price(self, bike):
		bike_cost = bike.total_cost()
		bike_cost = bike_cost * self.margin
		return	 bike_cost
##not part of 6/22 check##########################
	def sell_bike(self, bike):
		self.sold_bikes.append(bike)
		return self.sold_bikes

	def total_profit(self):
		total_profit = 0.0
		for bike in self.sold_bikes:
			bike_cost = bike.total_cost()
			total_profit += (bike_cost * self.margin) - (bike_cost)
		print("The total profit of bikes sold is {}".format(total_profit) + "\n")

#everything good until this point 6/22
class Customer(object):
	def __init__(self, name, funds):
		self.name = name
		self.funds = funds

	def eligible(self, bike, shop):
		cost_of_bike = shop.bike_sale_price(bike)
		if (self.funds >= cost_of_bike):
			return True

	def bike_range(self, shop):
		self.range = []
		for bike in shop.inventory:
			if self.eligible(bike, shop) == True:
				self.range.append(bike.name)

		print("Eligible bikes for {}: {}".format(self.name, self.range))

	def purchase_bike(self, bike, shop):
		cost_of_bike = shop.bike_sale_price(bike)
		print cost_of_bike
		print self.funds
		if (self.funds >= cost_of_bike): #why will it not work properly for (cost_of_bike >= self.funds)
			funds_left = self.funds - cost_of_bike
			print ("{} purchased, you have {}".format(bike.name, funds_left))
		else:
			print("You do not have enough money.")

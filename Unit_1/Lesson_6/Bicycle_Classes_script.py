'''
import Wheels
import Frame
import Manufacturer
import Bicycle_Model
import Bike_Shop
'''
type1 = Wheels('type1', 2, 100)
carbon = Frame(5, 500, 'carbon')
man1 = Manufacturer('man1', 20)
model1 = Bicycle_Model('model1', type1, carbon, man1)
vshop = Bike_Shop('vshop', 20)
v = Customer('Vivek', 1000.00)

vshop.inventory.append(model1)
#this will add a bike model to the inventory

for bike in vshop.inventory:
	#return the names of all bikes in inventory
	print ("{} is in the inventory".format(bike.name))

for bike in vshop.inventory:
	#returns the total cost of each of the bikes in the inventory
	print("{} is the cost of {}".format(bike.total_cost(), bike.name))

vshop.sell_bike(model1)

for bike in vshop.sold_bikes:
	print("A {} has been sold".format(bike.name))

vshop.total_profit()

v.purchase_bike(model1, vshop)



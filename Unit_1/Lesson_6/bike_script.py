import bike
from bike import Wheels
from bike import Frame 
from bike import Manufacturer 
from bike import Bicycle_Model
from bike import Bike_Shop
from bike import Customer 


'''
Creates two bicycle manufacturers, which both produce three different bicycle models 
(note that this implicitly requires you to create the wheels and frames that both manufacturers will need to produce their bicycles)
'''
#the wheels
x_wheel = Wheels('x_wheel', 6, 20)
y_wheel = Wheels('y_wheel', 4, 30)
z_wheel = Wheels('z_wheel', 2, 40)

#the frames
steel = Frame('steel', 20, 100)
aluminum = Frame('aluminum', 18, 200)
carbon = Frame('carbon', 15, 400)

#the manufacturers
viper = Manufacturer('viper', 18)
trident = Manufacturer('trident',19)

#bike_model
trident_x = Bicycle_Model('trident_x', x_wheel, steel, trident)
trident_y = Bicycle_Model('trident_y', y_wheel, aluminum, trident)
trident_z = Bicycle_Model('trident_z', z_wheel, carbon, trident)

viper_x = Bicycle_Model('viper_x', x_wheel, steel, viper)
viper_y = Bicycle_Model('viper_y', y_wheel, aluminum, viper)
viper_z = Bicycle_Model('viper_z', z_wheel, carbon, viper)

#for my testing
#print ("{},{},{}".format(trident_z.name, trident_z.total_weight(), trident_z.total_cost()))
#print ("{}, {}, {}".format(viper_z.name, viper_z.total_weight(), viper_z.total_cost()))

'''
Creates one bicycle shop that has 6 different bicycle models in stock, 3 from each manufacturer. 
The bicycle shop should charge its customers 20% over its cost for buying the bikes from the manufacturers.
'''
awesome_bikes = Bike_Shop("awesome_bikes", 20)
awesome_bikes.inventory = [trident_x, trident_y, trident_z, viper_x, viper_y, viper_z]

#for my testing
#print awesome_bikes.bike_sale_price(viper_z)

'''
Creates three customers. One customer has a budget of $200, the second $500, and the third $1000.
'''
kyle = Customer("kyle", 200.00)
jen = Customer("jen", 500.00)
vince = Customer("vince", 1000.00)

'''
Prints the name and total weight of each bicycle model carried by the bike shop
'''
awesome_bikes.show_inventory()
print"\n"
print"\n"

'''
Prints the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
Make sure you price the bikes in such a way that each customer can afford at least one.
'''
'''
NOTE TO MIKE:
I am having issues with my bike_range function. It is not performing as I would like it to, the available funds amount is too low for vince in order to get
a model_z bike
'''
kyle.bike_range(awesome_bikes)
jen.bike_range(awesome_bikes)
vince.bike_range(awesome_bikes)
print"\n"

'''
Prints the initial inventory of the bike shop for each bike it carries.
'''
awesome_bikes.initial_inventory()
print "\n"

'''
Has each of the three customers purchase a bike then prints the name of the bike the customer purchased, the cost, 
and how much money they have left over in their bicycle fund.
'''
kyle.purchase_bike(trident_x, awesome_bikes)
jen.purchase_bike(trident_y, awesome_bikes)
vince.purchase_bike(viper_x, awesome_bikes)

'''
After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, 
and how much profit they have made selling the three bikes.
'''

for bike in awesome_bikes.inventory:
	print(bike.name)

awesome_bikes.total_profit()

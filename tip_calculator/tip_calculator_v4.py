from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal_price", dest = "base_meal_price", type = "float", help = "base cost of the meal")
parser.add_option("-t", "--tip", dest = "tip_rate", type = "float")
parser.add_option("-r", "--tax", dest = "tax_rate", type = "float", help = "percent tip to leave", default = .15)

(options, args) = parser.parse_args()
if not options.base_meal_price:
	parser.error("Please enter the base price of the meal.")
if not options.tax_rate:
	parser.error("Please enter the tax rate")



base_meal_price = options.base_meal_price
tax_rate = options.tax_rate
tip_rate = options.tip_rate

tax_value = base_meal_price * (tax_rate)
meal_with_tax = base_meal_price + tax_value
tip_value = (tip_rate) * base_meal_price

total = meal_with_tax + tip_value

print "The base cost of the meal is ${0:.2f}.".format(base_meal_price)
print "The tax on your meal is ${0:.2f}.".format(tax_value)
print "The tip on your meal is ${0:.2f}.".format(tip_value)
print "The grand total for your meal is ${0:.2f}.".format(total)
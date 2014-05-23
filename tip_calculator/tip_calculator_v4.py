from optparse import OptionParser

parser = OptionParser()

parser.add_option("--m", "--meal_price", dest = "base_meal_price", type = "float")
parser.add_option("--t", "--tip", dest = "tip_rate", type = "float")
parser.add_option("--r", "--tax", dest = "tax_rate", type = "float")

(options, args) = parser.parse_args()



base_meal_price = options.base_meal_price
tax_rate = options.tax_rate/100.0
tip_rate = options.tip_rate/100.0

tax_value = base_meal_price * tax_rate
meal_with_tax = base_meal_price + tax_value
tip_value = tip_rate * base_meal_price

total = meal_with_tax + tip_value

print "The base cost of the meal is ${0:.2f}.".format(base_meal_price)
print "The tax on your meal is ${0:.2f}.".format(tax_value)
print "The tip on your meal is ${0:.2f}.".format(tip_value)
print "The grand total for your meal is ${0:.2f}.".format(total)
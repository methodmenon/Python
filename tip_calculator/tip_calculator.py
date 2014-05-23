base_meal_price = float(raw_input("What is the original price of the meal?"))
tax_rate = float(raw_input("What is the tax_rate?"))
tip_rate = float(raw_input("What is the tip rate?"))

tax_value = base_meal_price * tax_rate
meal_with_tax = base_meal_price + tax_value
tip_value = tip_rate * base_meal_price

total = meal_with_tax + tip_value

print "The base cost of the meal is {0}.".format(base_meal_price)
print "The tax on your meal is {0}.".format(tax_value)
print "The tip on your meal is {0}.".format(tip_value)
print "The grand total for your meal is {0}.".format(total)
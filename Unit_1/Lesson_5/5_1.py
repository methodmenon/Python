"""while True:
	try:
		n = int(raw_input("Enter an integer "))
		break
	except ValueError:
		print("Please enter an integer.")
"""
n = 100
print("Fizz buzz counting up to {0}".format(n))

for i in range(n + 1):
    if (i % 5 == 0):
        print "fizz buzz"
    elif (i % 3 == 0):
        print "fizz"
    else:
        print i
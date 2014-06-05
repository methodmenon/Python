import sys
arg_number = len(sys.argv)

if arg_number == 2:
	while True:
		try:
			n = int(sys.argv[1])
			break
		except ValueError:
			break
	else:
		while True:
			try:
				n = int(raw_input("Enter an integer "))
				break
			except ValueError:
				print("Please enter a valid integer")
else:
	while True:
		try:
			n = int(raw_input("Enter an integer "))
			break
		except ValueError:
			print("Please enter a valid integer")



print("Fizz buzz counting up to {0}".format(n))

for i in range(n + 1):
    if (i % 5 == 0):
        print "fizz buzz"
    elif (i % 3 == 0):
        print "fizz"
    else:
        print i
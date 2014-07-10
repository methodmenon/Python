import logging
import csv
import sys
import argparse

#set the log output file, and set the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

'''Write a function that
1) Opens a CSV file for writing
2) Write a snippet of text, with an associated name to the CSV file
'''

def put(name, snippet, filename):
	'''Store a snippet with the associated name into the CSV file'''
	#write messages to the log with the corresponding severity
	logging.info("Writing {}:{} to {}".format(name, snippet,filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		#using "a" argument so that information will be appended to the file OR a new file created in case it doesn't exist
		# create a new writer object to add a row to CSV file for each snippet created
		writer = csv.writer(f)
		logging.debug("Writing snippet to file".format(name, snippet))
		#writerow method of a writer object, adds a new row to the file
		writer.writerow([name, snippet])
		#pass in a list into the object, each value of list stored as a seperate column in the file
	logging.debug("Write sucessful")
	return name, snippet

def make_parser():
	"""construct the command line parser"""
	logging.info("Constructing Parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description = description)

	#add_subparsers method --> allows us to add multiple subparsers
	subparsers = parser.add_subparsers(help = "Available commands")

	#subparser for the put command
	logging.debug("Constructing put subparser")
	#use subparser's add_parser method to create a new subparser
	put_parser = subparsers.add_parser("put", help = "Store a snippet")
	#use add_argument method to add 3 positional arguments
	put_parser.add_argument("name", help = "name of the snippet")
	put_parser.add_argument("snippet", help = "the snippet text")
	#for filename argument, give 2 additional options:
	# i)use default argument to set the default filename
	# ii) nargs="?" option --> states we can leave out argument if we only want the default value
	put_parser.add_argument("filename", default = "snippets.csv", nargs= "?", help = "The snippet filename")
	put_parser.set_defaults(command = "put")
	return parser

def main():
	'''Main function'''
	logging.info("Starting snippets")
	#create a command line parser
	parser = make_parser()
	#call the parse_args method of parser to pass in all the command line args except the first one (which is program's name--don't want to parse)
	arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
	main()


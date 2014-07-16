import sys
import argparse
import logging
import csv
from collections import Counter

def get(name, filename):
	"""retrieve snippet with associated name from the CSV file"""
	reader = csv.reader(filename, delimiter = ",")
	for row in reader:
		print row[1]
	'''
		if name in row.keys():
			print (row[name])
		else:
			print ("this name does not exist")'''
if __name__ == "__main__":
	with open("snippets.csv") as f_obj:
		get("spam", f_obj)
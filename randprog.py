"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Creation of random programs for Popeel, the potato-peeling toy "software robot"

Todo: write on a file (and run it?)
"""

from random import randrange

def prog(name, ind, f):
	s = randrange(9)
	print(s)
	if s < 2:
		f.write(" "*ind + name + ".refill_basket()\n")	
	elif s < 4:
		f.write(" "*ind + name + ".peel_1_potato()\n")
	elif s == 4:
		f.write(" "*ind + name + ".discard_basket()\n")
	elif s == 5:
		f.write(" "*ind + name + ".go_sleep()\n")
	elif s == 6:
		wh_st(name, ind, f)
	elif s == 7:
		if_st(name, ind, f)
	else:
		prog(name, ind, f)
		prog(name, ind, f)

def wh_st(name, ind, f):
	f.write(" "*ind + "while " + cond(name) + ":\n")
	prog(name, ind+2, f)

def if_st(name, ind, f):
	f.write(" "*ind + "if " + cond(name) + ":\n")
	prog(name, ind+2, f)
	if randrange(5) == 0:
		f.write(" "*ind + "else:\n")
		prog(name, ind+2, f)

def cond(name):
	s = randrange(12)
	if s == 0:
		return cond(name) + " and " + cond(name)
	elif s == 1:
		return cond(name) + " or " + cond(name)
	elif s < 4:
		return "not " + cond(name)
	if s < 8:
		return name + ".basket_is_empty()"
	else:
		return name + ".enough_potatoes()"


name = "popeeler"
filename = "rand_popeel_1242.py"

with open(filename,"w") as f:
	f.write("from popeel import Popeel\n")
	f.write(name + " = Popeel()\n")
	prog(name, 0, f)
	

"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Creation of random programs for Popeel, the potato-peeling toy "software robot"

Todo: write on a file (and run it?)
"""

from random import randrange

def prog(name, ind):
	s = randrange(9)
	if s < 2:
		print(" "*ind + name + ".refill_basket()")	
	elif s < 4:
		print(" "*ind + name + ".peel_1_potato()")
	elif s == 4:
		print(" "*ind + name + ".discard_basket()")
	elif s == 5:
		print(" "*ind + name + ".go_sleep()")
	elif s == 6:
		wh_st(name, ind)
	elif s == 7:
		if_st(name, ind)
	else:
		prog(name, ind)
		prog(name, ind)

def wh_st(name, ind):
	print(" "*ind + "while " + cond(name) + ":")
	prog(name, ind+2)

def if_st(name, ind):
	print(" "*ind + "if " + cond(name) + ":")
	prog(name, ind+2)
	if randrange(5) == 0:
		print(" "*ind + "else:")
		prog(name, ind+2)

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

print("from popeel import Popeel")
print(name + " = Popeel()")
prog(name, 0)

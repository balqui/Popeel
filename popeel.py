"""
Author: Jose L Balcazar, ORCID 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Popeel, a potato-peeling toy software "robot"
"""

from random import randrange

DEFAULTTASK = 50 # if no task specified, default is to peel 50 potatoes

def _create_message(m, mm=''):
	r = "[Popeel says:] " + m 
	if mm:
		r += "\n               " + mm
	return r

class Popeel:
	
	def __init__(self):
		self.task = DEFAULTTASK
		self.sleeping = False
		self.potatoes = 0
		if randrange(5) == 0:
			self.basket = 0
		else:
			self.basket = randrange(1, 16)
		

	def task(n):
		"set task to peeling n potatoes"
		self.task = n
	
	def peel_1_potato(self):
		if self.sleeping:
			return
		if self.basket > 0:
			self.potatoes += 1
			self.basket -= 1
			if (self.task - self.potatoes) % 10 == 0:
				mm = "I have " + str(self.potatoes) + " peeled potatoes now."
			else:
				mm = ""
			print _create_message("Peeling one potato.", mm)
			if self.basket == self.task:
				print _create_message("I have completed my task.",
									"I LIKE that very much. :-)")
		else:
			print _create_message("I'm asked to peel one potato but I have no potatoes left in the basket.",
								"CAN'T DO IT. I go sleeping instead.")
		
	def refill_basket(self):
		if self.sleeping:
			return
		if self.basket > 0:
			print _create_message("I HATE to be sent for potatoes when I still have " + str(self.basket) + " left. :-(")
		else:
			self.basket = randrange(5, 30)
			print _create_message("Fetched more potatoes.", "I have now " + str(self.basket) + " of them. :-)")
			
	def go_sleep(self):
		self.sleeping = True
		print _create_message("I go sleeping. Goodnight.")
		
	def discard_basket(self):
		if self.sleeping:
			return
		print _create_message("Returning " + str(self.basket) + " potatoes to the main store. :-)")
		self.basket = 0
	
	def basket_is_empty(self):
		if self.sleeping:
			return
		return 



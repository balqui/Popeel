"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Popeel, a potato-peeling toy "software robot"
"""

from random import randrange

DEFAULTTASK = 45 # if no task specified, default is to peel 45 potatoes
MAXINIT = 15 # maximum of potatoes in basket upon creation

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
			self.basket = 1 + randrange(MAXINIT)
		if self.basket == 0:
			print(_create_message("Starting out with no potatoes in my basket."))
		else:
			print(_create_message("Starting out with " + str(self.basket) + " potatoes in my basket."))

	def set_task(self, n):
		"set task to peeling n potatoes"
		self.task = n
		print(_create_message("My task now is to peel " + str(n) + " potatoes."))
	
	def peel_1_potato(self):
		if self.sleeping:
			return
		if self.basket > 0:
			self.potatoes += 1
			self.basket -= 1
			if (self.task - self.potatoes) % 10 == 0:
				mm = str(self.potatoes) + " peeled potatoes so far."
			else:
				mm = ""
			print(_create_message("Peeling one potato.", mm))
			if self.potatoes == self.task:
				print(_create_message("Task completed.",
									"I LIKE that very much. :-)"))
		else:
			print(_create_message("Asked to peel one potato but no potatoes left in the basket.",
								"CAN'T DO IT. I go sleeping instead. Goodnight."))
			self.sleeping = True

	def refill_basket(self):
		if self.sleeping:
			return
		if self.basket > 0:
			print(_create_message("I HATE to be sent for potatoes when I still have " + str(self.basket) + " left. :-("))
		else:
			print(_create_message("I don't have any potatoes in my basket."))
			self.basket = randrange(5, 25)
			print(_create_message("Fetched more potatoes.", "I have now " + str(self.basket) + " of them. :-)"))

	def go_sleep(self):
		if self.sleeping:
			print(_create_message("Already fast asleep, sorry."))
		else:
			self.sleeping = True
			print(_create_message("I go sleeping. Goodnight."))
		
	def discard_basket(self):
		if self.sleeping:
			print(_create_message("You woke me up! Shame on you. Back to sleep. Goodnight."))
			return
		if self.basket > 0:
			print(_create_message("Returning " + str(self.basket) + " potatoes to the main store. :-)"))
		self.basket = 0
	
	def basket_is_empty(self):
		if self.sleeping:
			print(_create_message("You woke me up! Shame on you. Back to sleep. Goodnight."))
		return self.basket == 0

	def enough_potatoes(self):
		if self.sleeping:
			print(_create_message("You woke me up! Shame on you. Back to sleep. Goodnight"))
		return self.potatoes == self.task

if __name__ == "__main__":
	
	p = Popeel()
	p.set_task(23)
	if p.basket_is_empty():
		print("NO POTATOES IN BASKET.")
	else:
		print("SOME POTATOES IN BASKET.")
	if p.enough_potatoes():
		print("ENOUGH POTATOES.")
	else:
		print("NOT ENOUGH POTATOES.")
	p.refill_basket()
	p.peel_1_potato()
	p.peel_1_potato()
	p.peel_1_potato()
	p.peel_1_potato()
	p.peel_1_potato()
	p.discard_basket()
	p.go_sleep()
	if p.basket_is_empty():
		print("NO POTATOES IN BASKET.")
	else:
		print("SOME POTATOES IN BASKET.")
	if p.enough_potatoes():
		print("ENOUGH POTATOES.")
	else:
		print("NOT ENOUGH POTATOES.")


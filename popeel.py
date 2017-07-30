"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Early versions nov 2016; std class feb, jul 2017; singleton jul 2017

Popeel, a potato-peeling toy "software robot"
* class Popeel, for fully standard usage
* class Popeel_, singleton-like, can be used without instantiation
  or through standard usage via a single instance, but will refuse 
  creating further instances, or to create one once used without
"""

from random import randrange

DEFAULTTASK = 35 # if no task specified, default is to peel 35 potatoes
MAXINIT = 15 # maximum of potatoes in basket upon creation
WOKEUP = "You woke me up! Shame on you. Back to sleep. Goodnight."

class Popeel:
	"""
	Standard class for declaring potato-peeling robots
	"""

	@staticmethod
	def _create_message(m, mm=''):
		r = "[Popeel says:] " + m 
		if mm:
			r += "\n               " + mm
		return r

	def __init__(self):
		self.task = DEFAULTTASK
		self.sleeping = False
		self.potatoes = 0
		if randrange(5) == 0:
			self.basket = 0
		else:
			self.basket = 1 + randrange(MAXINIT)
		if self.basket == 0:
			print(self._create_message("Starting out with no potatoes in my basket."))
		else:
			print(self._create_message("Starting out with " + str(self.basket) + " potatoes in my basket."))

	def set_task(self, n = None):
		"set task to peeling n potatoes"
		if self.sleeping:
			self.sleeping = False
		if n is not None:
			self.task = n
			print(self._create_message("My task now is to peel " + str(n) + " potatoes."))
		else:
			"task 0 will never be completed"
			self.task = 0
			print(self._create_message("I have not been assigned a concrete task yet."))

	def peel_1_potato(self):
		if self.sleeping:
			print(self._create_message(WOKEUP))
			return
		if self.basket > 0:
			self.potatoes += 1
			self.basket -= 1
			if (self.task - self.potatoes) % 10 == 0:
				mm = str(self.potatoes) + " peeled potatoes so far."
			else:
				mm = ""
			print(self._create_message("Peeling one potato.", mm))
			if self.potatoes == self.task:
				"will never happen if task is zero"
				print(self._create_message("Task completed.",
									"I LIKE that very much. :-)"))
		else:
			print(self._create_message("Asked to peel one potato but no potatoes left in the basket.",
								"CAN'T DO IT. I go sleeping instead. Goodnight."))
			self.sleeping = True

	def refill_basket(self):
		if self.sleeping:
			print(self._create_message("Already fast asleep, sorry."))
			return
		if self.basket > 0:
			print(self._create_message("I HATE to be sent for potatoes when I still have " + str(self.basket) + " left. :-("))
		else:
			print(self._create_message("I don't have any potatoes in my basket."))
			self.basket = randrange(5, 30)
			print(self._create_message("Fetched more potatoes.", "I have now " + str(self.basket) + " of them. :-)"))

	def go_sleep(self):
		if self.sleeping:
			print(self._create_message("Already fast asleep, sorry."))
		else:
			self.sleeping = True
			print(self._create_message("I go sleeping. Goodnight."))
		
	def discard_basket(self):
		if self.sleeping:
			print(self._create_message(WOKEUP))
			return
		if self.basket > 0:
			print(self._create_message("Returning " + str(self.basket) + " potatoes to the main store. :-)"))
		self.basket = 0
	
	def is_basket_empty(self):
		if self.sleeping:
			print(self._create_message(WOKEUP))
		return self.basket == 0

	def enough_potatoes(self):
		if self.sleeping:
			print(self._create_message(WOKEUP))
		return self.potatoes == self.task

class Popeel_:
	"""
	Singleton-like class to be used as a single potato-peeling robot
	Designed so that it can be used in teaching object orientation
	before introducing variables
	"""

	sleeping = None
	task = DEFAULTTASK
	potatoes = 0

	if randrange(5) == 0:
		basket = 0
	else:
		basket = 1 + randrange(MAXINIT)

	@staticmethod
	def _create_message(m, mm=''):
		r = "[Popeel says:] " + m 
		if mm:
			r += "\n               " + mm
		return r

	def __init__(self):
		"""
		Accept one instance, and only before doing anything
		Detect sleeping being not None
		"""
		assert self.sleeping is None, ("\n\nSORRY. Instantiating Popeel_ here is disallowed."
							  "\nPlease use at most one instance and, if any, start with it.")
		cls = self.__class__
		cls.sleeping = False

	@classmethod
	def set_task(self, n = None):
		"set task to peeling n potatoes"
	def set_task(cls, n):
		"set task to peeling n potatoes"
		if cls.sleeping is None or cls.sleeping:
			cls.sleeping = False
		if cls.basket == 0:
			print(cls._create_message("Starting out with no potatoes in my basket."))
		else:
			print(cls._create_message("Starting out with " + str(cls.basket) + " potatoes in my basket."))

		if n is not None:
			cls.task = n
			print(cls._create_message("My task now is to peel " + str(n) + " potatoes."))
		else:
			"task 0 will never be completed"
			cls.task = 0
			print(cls._create_message("I have not been assigned a concrete task yet."))

	@classmethod
	def peel_1_potato(cls):
		if cls.sleeping is None:
			cls.sleeping = False
		elif cls.sleeping:
			print(cls._create_message(WOKEUP))
			return
		if cls.basket > 0:
			cls.potatoes += 1
			cls.basket -= 1
			if (cls.task - cls.potatoes) % 10 == 0:
				mm = str(cls.potatoes) + " peeled potatoes so far."
			else:
				mm = ""
			print(cls._create_message("Peeling one potato.", mm))
			if cls.potatoes == cls.task:
				print(cls._create_message("Task completed.",
									"I LIKE that very much. :-)"))
		else:
			print(cls._create_message("Asked to peel one potato but no potatoes left in the basket.",
								"CAN'T DO IT. I go sleeping instead. Goodnight."))
			cls.sleeping = True

	@classmethod
	def refill_basket(cls):
		if cls.sleeping:
			print(cls._create_message(WOKEUP))
			return
		if cls.basket > 0:
			print(cls._create_message("I HATE to be sent for potatoes when I still have " + str(cls.basket) + " left. :-("))
		else:
			print(cls._create_message("I don't have any potatoes in my basket."))
			cls.basket = randrange(5, 30)
			print(cls._create_message("Fetched some more potatoes.", "I have now " + str(cls.basket) + " of them. :-)"))

	@classmethod
	def go_sleep(cls):
		if cls.sleeping:
			print(cls._create_message("Already fast asleep, sorry."))
		else:
			cls.sleeping = True
			print(cls._create_message("I go sleeping. Goodnight."))
		
	@classmethod
	def discard_basket(cls):
		if cls.sleeping:
			print(cls._create_message(WOKEUP))
			return
		if cls.basket > 0:
			print(cls._create_message("Returning " + str(cls.basket) + " potatoes to the main store. :-)"))
		cls.basket = 0
	
	@classmethod
	def is_basket_empty(cls):
		if cls.sleeping:
			print(cls._create_message(WOKEUP))
		return cls.basket == 0

	@classmethod
	def enough_potatoes(cls):
		if cls.sleeping:
			print(cls._create_message(WOKEUP))
		return cls.potatoes == cls.task

if __name__ == "__main__":
	"""
	Test first an instance of the standard class, then the singleton-like one
	Alternatively, test the singleton-like one without instantiation
	"""
	for cls in [Popeel, Popeel_]:
		print("Test instance of ", str(cls))
		p = cls()
		p.set_task(23)
		if p.is_basket_empty():
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
		if p.is_basket_empty():
			print("NO POTATOES IN BASKET.")
		else:
			print("SOME POTATOES IN BASKET.")
		if p.enough_potatoes():
			print("ENOUGH POTATOES.")
		else:
			print("NOT ENOUGH POTATOES.")

	print("Test without instantiations")

	Popeel_.set_task(20)
	if Popeel_.is_basket_empty():
		print("NO POTATOES IN BASKET.")
	else:
		print("SOME POTATOES IN BASKET.")
	if Popeel_.enough_potatoes():
		print("ENOUGH POTATOES.")
	else:
		print("NOT ENOUGH POTATOES.")
	Popeel_.refill_basket()
	Popeel_.peel_1_potato()
	Popeel_.peel_1_potato()
	Popeel_.discard_basket()
	Popeel_.go_sleep()
	if Popeel_.is_basket_empty():
		print("NO POTATOES IN BASKET.")
	else:
		print("SOME POTATOES IN BASKET.")
	if Popeel_.enough_potatoes():
		print("ENOUGH POTATOES.")
	else:
		print("NOT ENOUGH POTATOES.")
	

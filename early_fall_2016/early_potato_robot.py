
from random import randint

class Potato_Robot:
	"simulation of a robot that fetches potatoes and peels them"
	
	def __init__(self, total_needed, verbose = False):
		self.basket = 0
		self.total_needed = total_needed
		self.peeled = 0
		self.tracing = False
		self.verbose = verbose
	
	def load_potatoes(self):
		"fetch some potatoes from a large repository"
		if self.basket > 0:
			raise Exception("Don't want to go for potatoes," 
							" I still have some left!") 
		else:
			self.basket = randint(10, 50)
			if self.verbose:
				print("Grabbed " + str(self.basket) + " potatoes.")

	
	def peel_1_potato(self):
		if self.basket > 0:
			self.basket -= 1
			self.peeled += 1
			if self.verbose:
				print("Peeled " + str(self.peeled) + 
					" potatoes and have " + str(self.basket) + " left.")
		else:
			raise Exception("Don't have any potato to peel!") 
	
	def enough_potatoes(self):
		"check whether we have peeled sufficient potatoes"
		return self.peeled >= self.total_needed

	def have_potatoes(self):
		"check whether we have some potato to peel"
		return self.basket > 0
	
	
	

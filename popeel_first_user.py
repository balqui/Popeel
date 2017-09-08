"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Usage of Popeel: simpler problem of peeling all potatoes in the basket.
"""

from popeel import Popeel

p = Popeel() # will tell us how many potatoes are in the basket initially

while not p.basket_is_empty():
	p.peel_1_potato()

p.go_sleep()



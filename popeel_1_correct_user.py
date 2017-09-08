"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

One correct usage of Popeel_ (feb, jul 2017).

Spoiler. 

Don't read this code.
"""

from popeel import Popeel_

p = Popeel_()
p.set_task(12)
while not p.enough_potatoes():
	if p.is_basket_empty():
		p.refill_basket()
	p.peel_1_potato()
p.discard_basket()
p.go_sleep()

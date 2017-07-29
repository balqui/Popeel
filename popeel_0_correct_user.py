"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

One correct usage of Popeel (feb, jul 2017).

Spoiler. 

Don't read this code.
"""

from popeel import Popeel_

Popeel_.set_task(12)
while not Popeel_.enough_potatoes():
	if Popeel_.is_basket_empty():
		Popeel_.refill_basket()
	Popeel_.peel_1_potato()
Popeel_.discard_basket()
Popeel_.go_sleep()

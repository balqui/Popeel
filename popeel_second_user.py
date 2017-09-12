"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Usage of Popeel: simple problem of peeling two basketfulls of potatoes.
"""

from popeel import Popeel

while not Popeel.is_basket_empty():
	Popeel.peel_1_potato()

Popeel.refill_basket()

while not Popeel.is_basket_empty():
	Popeel.peel_1_potato()

Popeel.go_sleep()



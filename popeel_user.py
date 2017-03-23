"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 (feb 2017)
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Usage of Popeel: example.
"""

from popeel import Popeel

p = Popeel() # will tell us how many potatoes are in the basket initially

p.set_task(8) # set the task: please peel 8 potatoes

p.peel_1_potato() # main operation, peels one potato from the basket

print(p.enough_potatoes()) # Boolean: task achieved?

print(p.basket_is_empty()) # Boolean: is Popeel's basket out of potatoes?

print(not p.basket_is_empty()) # Boolean: does Popeel still have potatoes in the basket?

p.refill_basket() # go to the main store and fetch some potatoes with the basket

p.discard_basket() # returns potatoes from the basket to the main store

p.go_sleep() # Popeel is asleep from that point on


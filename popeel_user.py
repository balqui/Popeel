"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Usage of Popeel: example (jul 2017).
"""

from popeel import Popeel

Popeel.set_task(8) # set the task: please peel 8 potatoes

Popeel.peel_1_potato() # main operation, peels one potato from the basket

Popeel.refill_basket() # go to the main store and fetch some potatoes with the basket

Popeel.discard_basket() # returns potatoes from the basket to the main store

Popeel.enough_potatoes() # Boolean: task achieved?

Popeel.is_basket_empty() # Boolean: is Popeel's basket out of potatoes?

Popeel.go_sleep() # Popeel is asleep from that point on



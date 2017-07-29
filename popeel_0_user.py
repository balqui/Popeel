"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Usage of Popeel_ with no instances: example (jul 2017).
"""

from popeel import Popeel_

Popeel_.set_task(8) # set the task: please peel 8 potatoes

Popeel_.peel_1_potato() # main operation, peels one potato from the basket

Popeel_.refill_basket() # go to the main store and fetch some potatoes with the basket

Popeel_.discard_basket() # returns potatoes from the basket to the main store

Popeel_.enough_potatoes() # Boolean: task achieved?

Popeel_.is_basket_empty() # Boolean: is Popeel's basket out of potatoes?

Popeel_.go_sleep() # Popeel is asleep from that point on



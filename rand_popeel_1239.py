from popeel import Popeel
popeeler = Popeel()
if popeeler.enough_potatoes():
  popeeler.refill_basket()
else:
  while popeeler.enough_potatoes() or popeeler.is_basket_empty() and popeeler.enough_potatoes() and not popeeler.enough_potatoes():
    popeeler.refill_basket()
  if popeeler.basket_is_empty():
    while popeeler.enough_potatoes():
      popeeler.peel_1_potato()
      popeeler.refill_basket()
      popeeler.go_sleep()
    popeeler.peel_1_potato()

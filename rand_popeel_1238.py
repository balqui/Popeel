from popeel import Popeel
popeeler = Popeel()
while popeeler.basket_is_empty():
  if not popeeler.basket_is_empty():
    popeeler.discard_basket()
  else:
    popeeler.refill_basket()

from popeel import Popeel
popeeler = Popeel()
while popeeler.is_basket_empty():
  if not popeeler.is_basket_empty():
    popeeler.discard_basket()
  else:
    popeeler.refill_basket()

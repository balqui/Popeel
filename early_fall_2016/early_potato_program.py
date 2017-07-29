
from e0240_0_potato_robot import Potato_Robot

robot = Potato_Robot(80, verbose=True) # robot must peel 200 potatoes

while not robot.enough_potatoes():
	if not robot.have_potatoes():
		robot.load_potatoes()
	robot.peel_1_potato()



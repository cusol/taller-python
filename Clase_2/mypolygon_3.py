from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, length, n):
	angle = 360.0/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)
	
polygon(bob,50,5)
wait_for_user()


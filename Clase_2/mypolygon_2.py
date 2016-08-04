from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)
	
square(bob,50)
wait_for_user()


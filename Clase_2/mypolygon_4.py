from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polygon(t, length, n):
	angle = 360.0/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def circle(t, r):
	circum = 2*math.pi*r
	n = 100
	lenght = circum/n
	polygon(t,lenght,n)
	
circle(bob,10)
wait_for_user()


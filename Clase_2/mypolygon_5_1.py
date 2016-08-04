from swampy.TurtleWorld import *
import math

#Reusar funciones ya implementadas

def polyline(t, n, length, angle):
    for i in range(n):
        fd( t, length)
        lt(t, angle)

def polygon(t,  n, length):
	angle = 360.0/n
	polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)
    
    
#Finally
def circle(t, r):
    arc(t, r, 360)

#anadir docstrings!    
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#arc(bob,20,90)
circle(bob, 50 )
wait_for_user()

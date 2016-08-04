from swampy.TurtleWorld import *
import math

#parecida a polygon pero para crear una aprox de arco.
def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = float(angle)/n
    
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
        
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

arc(bob,20,90)
wait_for_user()

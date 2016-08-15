#http://openbookproject.net/thinkcs/python/english3e/recursion.html
#http://openbookproject.net/thinkcs/python/english3e/conditionals.html
from swampy.TurtleWorld import *

def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
koch(bob, 200)

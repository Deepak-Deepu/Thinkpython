from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def polygon(t, n, length):
	angle = 360.0 /n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

print polygon(bob, 7, 70)
wait_for_user()

#
# numerical solution to the free throw problem
# https://youtu.be/Q8iHjLSyRpY

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
theta,t = symbols("theta t")

#parameters of the problem
g = 9.8
h = 8.5
d = 2.0
v0 = 20

#travel time to reach horizontal position of wall with the hole
eq1 = Eq(d,v0 * cos(theta) * t)  

#travel time to reach the 8.5 edge of the hole
eq2 = Eq(h,v0 * sin(theta) * t - 0.5 * g * t**2)

#solve for v and t
solution = solve((eq1, eq2), (theta, t))

#print solutions
#look for positive angles and convert to degrees
for pair in solution:
    if pair[0] > 0:
        print(f"{pair[0] * 180/pi.evalf()} degrees")

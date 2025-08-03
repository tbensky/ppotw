#
# numerical solution to the free throw problem
# https://youtu.be/ZE-JZX5pbFM

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
v,t = symbols("v t")

#parameters of the problem
g = 9.8
h1 = 8.5
h2 = 8.5 + 1.27
d = 2.0
theta = 80 * pi.evalf()/180


#travel time to reach horizontal position of wall with the hole
eq1 = Eq(d,v * cos(theta) * t)  

#travel time to reach the 8.5 edge of the hole
eq2 = Eq(h1,v * sin(theta) * t - 0.5 * g * t**2)

#solve for v and t
solution = solve((eq1, eq2), (t, v))

#print the result (find v>0 solutions)
for pair in solution:
    if pair[1] > 0:
        print(f"{pair[1]} m/s")


#now find the travel time to reach the 8.5 + 1.27 = 9.77 m edge
eq2 = Eq(h2,v * sin(theta) * t - 0.5 * g * t**2)

#solve for v and t
solution = solve((eq1, eq2), (t, v))

#print the result (find v>0 solutions)
for pair in solution:
    if pair[1] > 0:
        print(f"{pair[1]} m/s")

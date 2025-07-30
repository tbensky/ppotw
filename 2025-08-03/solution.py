#
# numerical solution to the free throw problem
# https://youtu.be/_VmvJGGCeRg

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
v,t = symbols("v t")

#parameters of the problem
g = 9.8
h0 = 3.1
y0 = 2.0
d = 7.5
theta = 48 * pi.evalf()/180

#travel time to reach horizontal position of bucket
eq1 = Eq(d,v * cos(theta) * t)  

#travel time to reach vertical position of bucket
eq2 = Eq(h0,y0 + v * sin(theta) * t - 0.5 * g * t**2)

#solve for v and t
solution = solve((eq1, eq2), (t, v))

#print the result
#solution will contain pairs of (t,v) solutions
#print the one with the positive v
for pair in solution:
    if pair[1] > 0:
        print(f"v={pair[1]} m/s")
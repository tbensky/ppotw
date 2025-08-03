#
# numerical solution to the free throw problem
# https://youtu.be/Jj4VzIojarg

from sympy import symbols, Eq, solve, sin, cos, pi, atan
import math

# Define variables
v,t = symbols("v t")

#parameters of the problem
g = 9.8
v0 = 5
theta = 70.0 * pi.evalf()/180.
theta_target = -89.9999999*pi.evalf()/180.

#travel time to reach horizontal position of bucket
eq1 = Eq(theta_target,atan((v0 * sin(theta) - g * t)/(v0 * cos(theta))))  

#solve for the angle
solution = solve(eq1, t)

#print the result
t = solution[0]
print(f"t={solution[0] /3.154e7} years")
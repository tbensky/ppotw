#
# numerical solution to two pendulums colling elastically
# https://youtu.be/cB-6sc0GlWY
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
v2f, theta = symbols('v2f theta')
m1 = 5
m2 = 2
L = 4
g = 9.8
theta0 = 40 * pi/180

#Solve for speed of left pendulum when it swings down
eq = Eq(m1 * g * L * (1-cos(theta0)),0.5 * m1 * v2f**2)
solution = solve(eq,v2f)
v1i = [v for v in solution if v > 0][0]
print(f"{v1i} m/s")

#get post collision speed of the right pendulum
v2i = 2 * m1 / (m1 + m2) * v1i
print(f"{v2i} m/s")

#get angle the right pendulum swings up to
eq = Eq(0.5 * m2 * v2i**2,m2 * g * L * (1-cos(theta)))
solution = solve(eq,theta)
print(f"{min([x*180/pi.evalf() for x in solution])} Degrees")
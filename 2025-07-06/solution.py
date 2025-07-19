#
# numerical solution to bounce height of ball bouncing 100 times
# https://youtu.be/nNtdsqTxzAs
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
vf, x, dt = symbols('vf x, dt')
m = 90
v = 15
g = 9.8
mu = 0.6
d = 10
h = 17

#first, find how long the sledder is going after the friction
eq = Eq(0.5 * m * v**2,mu * m * g * d + 0.5 * m * vf**2)
solution = solve(eq,vf)
vf = (v for v in solution if v > 0](0]
print(vf)

#now find hang time when over cliff
eq = Eq(0,h - 0.5 * g * dt**2)
solution = solve(eq,dt)
thang = (t for t in solution if t > 0](0]
print(thang)

#now find horizontal distance travelled in thang
d = vf * thang
print(f"d={d} meters from the edge")

   
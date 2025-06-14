#
# numerical solution to skier with spring and friction
# https://youtu.be/MSvbtBqpPvg
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
vf1, vf2, ds = symbols('vf1 vf2 ds')
m = 90
g = 9.8
h = 5
d = 0.5
mu = 0.25
k = 1000
v0 = 5

#initial energy: KE and PE of the skier
Ei = 0.5 * m * v0**2 + m * g * h

#
#method 1: do it all in one step: initial energy to final energy at A.
#
#final energy: KE and energy lost due to sliding over the friction TWICE
Ef = 0.5 * m * vf1**2 + mu * m * g * d + mu * m * g * d

#solve Ei=Ef
eq1 = Eq(Ei,Ef)

#find the solution for v at A
solution = solve(eq1, vf1)
vf1 = [v for v in solution if v > 0][0]
print(f"method 1: {vf1} m/s")

#
#method 2: do it in two steps. initial energy into the spring, then spring
#energy to energy at point A
#
#final energy: energy lost due to sliding over the friction and going into compressing the spring
Ef = mu * m * g * d + 0.5 * k * ds**2

#solve Ei=Ef
eq1 = Eq(Ei,Ef)

#find the solution for how much the spring compresses
solution = solve(eq1, ds)
ds = [ds for ds in solution if ds > 0][0]

#now use spring energy as Ei
Ei = 0.5 * k * ds**2

#final energy: energy lost due to sliding over the friction and into the KE at A
Ef = 0.5 * m * vf2**2 + mu * m * g * d

#solve Ei=Ef
eq1 = Eq(Ei,Ef)

#find the solution for how much the spring compresses
solution = solve(eq1, vf2)
vf2 = [v for v in solution if v > 0][0]
print(f"method 2: {vf2} m/s")
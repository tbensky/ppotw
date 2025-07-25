#
# numerical solution to bounce height of ball bouncing 100 times
# https://youtu.be/uhmyzuxY4TA

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
g = 9.8
y0 = 2.5
v0 = 10
theta = 40 * pi.evalf()/180
vx0 = v0 * cos(theta)
vy0 = v0 * sin(theta)
d0 = 11.5
h = 1

#find time to travel 11.5 m horizontally
tnet = 11.5 / vx0
yatnet= 2.5 + vy0 * tnet - 0.5 * g * tnet ** 2

#print the result
print(f"height when over net={yatnet} m.")
print(f"so this is {yatnet-h} m above the net.")

   
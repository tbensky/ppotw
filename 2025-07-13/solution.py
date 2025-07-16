#
# numerical solution to bounce height of ball bouncing 100 times
# https://youtu.be/-pcge71mipE
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
v0 = 4
g = 9.8
dt = 0.6

v = v0 - g * dt
print(f"v={v} m/s (- means down)")

   
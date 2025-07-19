#
# numerical solution to bounce height of ball bouncing 100 times
# https://youtu.be/xrOeUXGMLJ4
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
m = 7.0
dt = 5

#find the ax and y accelerations
ax = (+20*cos(math.radians(15))
    - 5*sin(math.radians(10))
    - 30*cos(math.radians(38))
    - 25*cos(math.radians(12))
    + 22*sin(math.radians(5))
    + 8)/m

ay = (+20*sin(math.radians(15))
    + 5*cos(math.radians(10))
    + 30*sin(math.radians(38))
    - 25*sin(math.radians(12))
    - 22*cos(math.radians(5)))/m

#initial speed
vx0 = -10*sin(math.radians(30))
vy0 = -10*cos(math.radians(30))

#predict 5 seconds into the future
vx = vx0 + ax * dt
vy = vy0 + ay * dt
v = math.sqrt(vx**2 + vy**2)
theta = 180 / pi.evalf() * math.atan(vy/vx)

#print the result
print(f"v={v} m/s, theta={theta}")

   
#
# numerical solution to 2 projectiles collidiing
# https://youtu.be/qxSlbuK7b1I
#

from sympy import symbols, Eq, solve, sin, cos, pi

# Define variables
dt, theta = symbols('dt theta')
PI = pi.evalf()

#values for this problem
g = 9.8
d = 25

#left cannon
vleft = 7
hleft = 10
theta_left = 15 * PI / 180

#right cannon
vright = 20
hright = 2

#set up equations for the x and y positions of each ball
#logic: look for a theta and time where xright=xleft and yright=yleft
eq1 = Eq(hleft + vleft * sin(theta_left) * dt - 0.5 * g * dt**2,hright + vright * sin(theta) * dt - 0.5 * g * dt**2)
eq2 = Eq(vleft * cos(theta_left),d - vright * cos(theta) * dt)

#find the solution
solution = solve((eq1,eq2], (dt,theta))
print(solution)

#pull out the positive solution for theta
for s in solution:
    if s(1] > 0:
        theta = s(1]

#print solution
print(theta * 180/PI)
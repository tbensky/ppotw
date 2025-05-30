#
# numerical solution to atwood machine with energy
# https://youtu.be/idhdRJ_a71M
#

from sympy import symbols, Eq, solve, sin, cos, pi

# Define variables
v = symbols('v')
PI = pi.evalf()

#values for this problem
g = 9.8
d = 25

m1 = 4
m2 = 11
h1 = 8
h2 = 6
g = 9.8
v0 = 4

#set up equations for the x and y positions of each ball
#logic: look for a theta and time where xright=xleft and yright=yleft
eq1 = Eq(0.5 * m1 * v0**2 + 0.5 * m2 * v0**2 + m1 * g * h1 + m2 * g * h2, 0.5 * m1 * v**2 + 0.5 * m2 * v**2 + m1 * g * (h1 + h2),)

#find the solution
solution = solve(eq1, v)
print(solution)
from sympy import symbols, Eq, solve, sin, cos, pi

# Define variables
m, F, g, mu, a, dx = symbols('m F g mu a dx')

#values for this problem
m = 90
g = 9.8
v0 = 15
mu = 0.4
theta = 25.0 * pi/180

#net force and acceleration
F = -m * g * sin(theta) - mu * m * g * cos(theta)
a = F / m

#solve kinematic equation, v^2=v0^2+2a(dx) for dx
eq1 = Eq(0,v0**2 + 2*a*dx)
solution = solve(eq1, (dx))
print(f"Solution:  {solution}")
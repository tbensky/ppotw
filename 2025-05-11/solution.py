from sympy import symbols, Eq, solve, sin, cos, pi

# Define variables
H, tup, tdown = symbols('H tup tdown')

#values for this problem
g = 9.8
H = 100

#set up equations for the rock, sound and total time
eq1 = Eq(0,H + 10 * tup - 0.5 * g * tup**2)
eq2 = Eq(0,H - 10 * tdown - 0.5 * g * tdown**2)

#find the solution
solution = solve([eq1,eq2], (tup,tdown))

#look for 2 positive times
sol = []
for s in solution:
    if all(x > 0 for x in s):
        sol = s

#find the time between the flight times
sol = sorted(sol)
dt = sol[1] - sol[0]
print(f"Solution:  {dt}")
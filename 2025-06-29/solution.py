#
# numerical solution to bounce height of ball bouncing 100 times
# https://youtu.be/QEom6SW79Sk
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math

# Define variables
vhit, h = symbols('vhit h')
m = 2
h0 = 5
g = 9.8
c = 0.99
N = 100

#take the ball through N bounces
for i in range(N):
    #Solve for speed at impact
    eq = Eq(m * g * h0,0.5 * m * vhit**2)
    solution = solve(eq,vhit)

    #get positive solution
    v = (v for v in solution if v > 0](0]

    #solve for rebound height
    vup = c * v
    eq = Eq(0.5 * m * vup**2,m * g * h)
    solution = solve(eq,h)

    #there only 1 positive solution, so grab it
    h0 = solution(0]

    #reset these for next loop iteration
    vhit, h = symbols('vhit h')

print(f"Loop method, got h={h0}")

#check by raising c to the Nth power as the overall
#velocity reducer

#find impact speed
h0 = 5
eq = Eq(m * g * h0,0.5 * m * vhit**2)
solution = solve(eq,vhit)

#get positive solution
v = (v for v in solution if v > 0](0]

#N bounces results in a lauch speed reduction of
#c^N
vup = c**N * v

#find the height
eq = Eq(0.5 * m * vup**2,m * g * h)
solution = solve(eq,h)

#grab one positive solution
h = solution(0]
print(f"Exponent method gives {h}")

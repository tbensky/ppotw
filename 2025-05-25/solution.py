#
# numerical solution to 2 clay balls rising and falling vertically, colliding and sticking
# https://youtu.be/C2eMeFgAFZI
#

from sympy import symbols, Eq, solve, sin, cos, pi

def get_positive(l):
    return (x for x in l if x > 0.0](0]

# Define variables
v1f, v2f, Vblob, hblob, hfinal = symbols('v1f v2f Vblob hblob hfinal')

#values for this problem
g = 9.8
m1 = 1
m2 = 5
v2i = 10
hcollide = 2
h1i = 10
h1f = 2

#get speed of m2 at collision point
eq = Eq(0.5 * m2 * v2i**2,m2 * g * hcollide + 0.5 * m2 * v2f**2)
solution = solve(eq,v2f)
v2f = get_positive(solution)
print(f"v2f={v2f}")

#and speed of m1 at collision point
eq = Eq(m1 * g * h1i,0.5 * m1 * v1f ** 2 + m1 * g * h1f)
solution = solve(eq, v1f)
v1f = get_positive(solution)
print(f"v1f={v1f}")

#find final speed of blob of clay after the collision
eq = Eq(-m1 * v1f + m2 * v2f,(m1 + m2) * Vblob)
solution = solve(eq, Vblob)
Vblob = get_positive(solution)
print(f"Vblib={Vblob}")

#see how high the blob goes after the collision
eq = Eq(0.5 * (m1 + m2) * Vblob**2 + (m1 + m2) * g * hcollide,(m1 + m2) * g * hfinal)
solution = solve((eq], (hfinal))
print(solution)

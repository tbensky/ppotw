#
# numerical solution to sledder with friction
# https://youtu.be/1ujUJkTgwwM
#

from sympy import symbols, Eq, solve, sin, cos, pi
import math
import matplotlib.pyplot as plt

# Define variables
m = 90
g = 9.8
h = 5
d = 1.5
mu = 0.4

#total energy
Etot = m*g*h

#energy lost per each pass over the friction (work due to friction)
Eloss = mu * m * g * d

#see how many passes can be sustained given total energy and loss per pass
passes = Etot / Eloss

#output some results
print(f"Passes over friction to stop: {passes}")
frac = passes - math.floor(passes)
print(f"After {math.floor(passes)} passes, the block will need another {frac:0.2f} fraction of a pass to stop.")
print(f"For a {d} m long patch of friction, this will be ({d})({frac:0.2f})={d*frac:0.2f} m from the left edge. ")

pass_count = 1
pc = [pass_count]
E = [Etot]
while Etot > 0:
    Etot -= Eloss
    E.append(Etot)
    pc.append(pass_count)
    pass_count += 1
    print(f"Pass={pass_count}, remaining energy={Etot}")

plt.plot(pc,E)
plt.xlabel("Pass count")
plt.ylabel("Energy left (J)")
plt.title("Energy loss as the sledder goes")
plt.grid(True)
plt.show()



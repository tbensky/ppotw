from sympy import symbols, Eq, solve, sin, cos, pi

# Define variables
D, t_rock_fall, t_sound_up = symbols('D t_rock_fall t_sound_up')

#values for this problem
g = 9.8
vsound = 343
T = 5

#set up equations for the rock, sound and total time
eq1 = Eq(0,D-0.5 * g * t_rock_fall**2)
eq2 = Eq(D,vsound * t_sound_up)
eq3 = Eq(t_rock_fall + t_sound_up, T)

#find the solution
solution = solve([eq1,eq2,eq3], (t_rock_fall,t_sound_up,D))
print(f"Solution:  {solution}")
import sys
import math
sys.path.append("../diophantine")

from diophantine_solver import diophantine_equ_solver

def congruence_equ_solver(a, mod, b):
    dioph = diophantine_equ_solver(a, mod, b)
    sol = []

    if dioph != {}:
        x_ind = dioph["x"][0] % mod
        t_coef = dioph["x"][1] % mod
        for t in range(math.gcd(a, mod)):
            x = (x_ind + t_coef * t) % mod
            if x >= 0 and x < mod:
                sol.append(x)
        sol.sort()
    return sol

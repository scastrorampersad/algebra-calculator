import sys
sys.path.append("../congruence")

from fractions import Fraction as frac
from congruence_solver import congruence_equ_solver

def num_mod(num, mod):
    if mod == 0:
        return num
    else:
        return num % mod

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def inverse_mod(num, mod):
    if mod == 0:
        return frac(1, num)
    else:
        inverse = congruence_equ_solver(num, mod, 1)
        if not bool(inverse):
            return 0
        else:
            return inverse[0]

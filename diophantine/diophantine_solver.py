import sys
sys.path.append("common")

from euclidean_alg import euclidean_alg
import numpy as np
import math

def diophantine_equ_solver(a, b, n):
    gcd = math.gcd(a, b)

    if gcd == 0 or n % gcd != 0:
        sol = {}
    else:
        multi_factor = n/gcd
        euc = euclidean_alg(a, b)
        x0 = euc["r"] * multi_factor
        y0 = euc["s"] * multi_factor

        sol = {
            "x": (int(x0), int(b/gcd)),
            "y": (int(y0), int(-a/gcd))
        }

    return sol

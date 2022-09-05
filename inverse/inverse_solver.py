import sys
sys.path.append("../common")

import numpy as np
from fractions import Fraction as Frac
from gauss_jordan import *
from elementary_matrix import *
from mod_operations import *

def inverse_solver(matrix, mod):
    dim = np.shape(matrix)[0]
    identity = I_matrix(dim)
    sol = {}

    if mod != 0:
        matrix = num_mod(matrix, mod)
    else:
        identity = identity + Frac()

    aug_matrix = np.concatenate((matrix, identity), axis = 1)
    aug_matrix = gauss(aug_matrix, mod)

    if aug_matrix[dim-1][dim-1] != 1:
        sol['exist'] = False
    else:
        aug_matrix = jordan(aug_matrix, mod)
        sol['exist'] = True
        sol['inverse']= np.hsplit(aug_matrix, 2)[1]

    return sol

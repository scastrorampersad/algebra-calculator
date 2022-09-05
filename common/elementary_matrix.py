import numpy as np
from mod_operations import *
from fractions import Fraction as frac

def I_matrix(dim):
    identity = np.zeros(shape = (dim, dim)).astype(int)

    for i in range(dim):
        identity[i][i] = 1

    return identity

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def swap(row1, row2, identity):
    arr = np.copy(identity)

    arr[[row1, row2]] = arr[[row2, row1]]

    return arr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def mult_row(row, coeff, identity, mod):
    arr = np.copy(identity)
    if mod != 0:
        arr[row][row] = coeff
    else:
        arr = arr + frac()
        arr[row][row] = coeff

    return arr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def add_mult_row(row1, row2, coeff, identity, mod):
    arr = np.copy(identity)
    if mod != 0:
        arr[row1][row2] = coeff
    else:
        arr = arr + frac()
        arr[row1][row2] = coeff

    return arr

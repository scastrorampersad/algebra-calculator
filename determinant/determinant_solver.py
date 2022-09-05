import sys
sys.path.append("../common")

import numpy as np
from mod_operations import *
from fractions import Fraction as Frac

def determinant_solver(matrix, mod):
    dim = np.shape(matrix)[0]
    cofactor = 1
    det = 0

    if dim == 1:
        det = num_mod(matrix[0][0], mod)
        return det
    else:
        for i in range(dim):
            if i%2 != 0:
                cofactor = -1
            else:
                cofactor = 1

            minor_matrix = np.delete(matrix, i, axis = 1 )
            minor_matrix = np.delete(minor_matrix, 0, axis = 0)
            comp_det = num_mod((cofactor*matrix[0][i]*determinant_solver(minor_matrix, mod)), mod)
            det += comp_det

        return num_mod(det, mod)

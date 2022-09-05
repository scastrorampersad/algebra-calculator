import numpy as np
from elementary_matrix import *
from mod_operations import *
from fractions import Fraction as frac

def gauss(matrix, mod):
    rows, colums = np.shape(matrix)
    identity = I_matrix(rows)

    if mod != 0:
        arr = num_mod(matrix, mod)
    else:
        arr = matrix + frac()

    arr = reorg_matrix(arr)

    if rows <= colums-1:
        dim = rows
    else:
        dim = colums-1

    for i in range(dim):
        if i != rows-1:
            arr = pivots(arr, i, mod, identity)
            arr = colum2ZeroT2B(arr, i, mod, identity)
            arr = reorg_matrix(arr)
        else:
            arr = pivots(arr, i, mod, identity)

    return arr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def jordan(matrix, mod):
    rows, colums = np.shape(matrix)
    identity = I_matrix(rows)
    k = 1

    for i in range(rows-1, 0, -1):
        for j in range(colums):
            if matrix[i][j] == 1:
                matrix = colum2ZeroB2T(matrix, j, k, mod, identity)
                break
        k += 1

    return matrix

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def pivots(matrix, rowIndex, mod, identity):
    for i in matrix[rowIndex]:
        if i != 0:
            matrix = num_mod(np.matmul(mult_row(rowIndex, inverse_mod(i, mod), identity, mod), matrix), mod)
            break

    return matrix

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def colum2ZeroT2B(matrix, colum, mod, identity):
    rows,colums = np.shape(matrix)

    for i in range(colum+1, rows):
        if matrix[i][colum] != 0:
            matrix = num_mod(np.matmul(add_mult_row(i, colum, -matrix[i][colum], identity, mod), matrix), mod)

    return matrix

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def colum2ZeroB2T(matrix, colum, k, mod, identity):
    rows,colums = np.shape(matrix)

    if rows >= colums-1:
        dim = colum
    else:
        dim = rows-k

    for i in range(dim-1,-1, -1):
        if matrix[i][colum] != 0:
            matrix = num_mod(np.matmul(add_mult_row(i, dim, -matrix[i][colum], identity, mod), matrix), mod)

    return matrix

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def reorg_matrix(matrix):

    matrix = matrix[np.lexsort(abs(np.transpose(matrix)[::-1]))]
    matrix = np.flip(matrix, 0)

    return matrix

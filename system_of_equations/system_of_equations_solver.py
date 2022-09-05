import sys
sys.path.append("../common")

import numpy as np
from fractions import Fraction as frac
from gauss_jordan import *

def system_of_equations_solver(matrix, mod):
    rows, colums = np.shape(matrix)
    matrix = gauss(matrix, mod)
    sol = {}
    type = system_type(matrix)

    if type == 'Inconsistent':
        sol["type"] = type
    elif type == 'Consistent independent':
        sol = solve_CIS(matrix, mod)
    else:
        sol = solve_CDS(matrix, mod)

    return sol

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def system_type(matrix):
    rows, colums = np.shape(matrix)
    rowIndex = rows-1
    columIndex = colums-1
    sum_last_row = np.sum(matrix[rowIndex])
    count = 0

    if sum_last_row != 0:
        if np.count_nonzero(matrix[rowIndex] == 0) == columIndex and matrix[rowIndex][columIndex] != 0:
            return 'Inconsistent'
        elif rows == colums-1:
            return 'Consistent independent'
        else:
            return 'Consistent dependent'
    else:
        while sum_last_row == 0:
            rowIndex -= 1
            count += 1
            sum_last_row = np.sum(matrix[rowIndex])
        if np.count_nonzero(matrix[rowIndex] == 0) == columIndex and matrix[rowIndex][columIndex] != 0:
            return 'Inconsistent'
        elif count == colums-1:
            'Consistent independent'
        else:
            return 'Consistent dependent'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_CIS(matrix, mod):
    matrix = jordan(matrix, mod)
    rows, colums = np.shape(matrix)
    sol = {"type": "Consistent independent"}

    for i in range(colums-1):
        sol["x"+str(i)] = matrix[i][colums-1]

    return sol

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_CDS(matrix,mod):
    matrix = jordan(matrix, mod)
    rows, colums = np.shape(matrix)
    sol = {"type": "Consistent dependent"}
    auxStr = ''
    aux = 0
    pivots = where_pivots(matrix)

    for i in range(colums-1):
        sol["x"+str(i)] = ''

    for i in pivots:
        for j in range(i[1]+1,colums-1):
                aux = num_mod(matrix[i[0]][j] * -1, mod)
                if aux != 0:
                    if aux >= 0:
                        auxStr = auxStr + '+' + str(aux) + 'x' + str(j)
                    else:
                        auxStr = auxStr + str(aux) + 'x' + str(j)
        aux = matrix[i[0]][colums-1]
        if aux > 0:
            auxStr = auxStr + '+' + str(aux)
        elif aux < 0:
            auxStr = auxStr + str(aux)
        sol["x"+str(i[1])] = auxStr
        auxStr = ''

    return sol

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def where_pivots(matrix):
    rows, colums = np.shape(matrix)
    pivots_pos = []

    for i in range(rows):
        for j in range(colums-1):
            if matrix[i][j] == 1:
                pivots_pos.append((i, j))
                break

    return pivots_pos

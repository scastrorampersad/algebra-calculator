from fractions import Fraction as Frac
import numpy as np

def matrix_parser(input, is_q):
    lines = input.split('\n')
    mat = []
    h = len(lines)
    function = int

    if is_q:
        function = Frac

    for l in lines:
        line = list(map(function, l.split()))
        if len(line) != h:
            raise ValueError('Invalid_dimention')
        mat.append(line)

    return np.array(mat)

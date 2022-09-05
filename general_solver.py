import sys
sys.path.append("diophantine")
sys.path.append("congruence")
sys.path.append("system_of_equation")
sys.path.append("determinant")
sys.path.append("inverse")
sys.path.append("parsers")

from diophantine_solver import diophantine_equ_solver
from diophantine_parser import diophantine_parser
from congruence_solver import congruence_equ_solver
from system_of_equations_solver import system_of_equations_solver
from system_of_equations_parser import system_of_equations_parser
from determinant_solver import determinant_solver
from inverse_solver import inverse_solver
from matrix_parser import matrix_parser

def get_diophantine_result(equation_str):
    data = diophantine_parser(input)
    return diophantine_equ_solver(data['x'], data['y'], data['n'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_congruence_result(equ_parms_str):
    return congruence_equ_solver(int(equ_parms_str['a']),
    int(equ_parms_str['mod']), int(equ_parms_str['b']))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_system_result(equations_str, mod):
    is_q = False if mod != 0 else True
    dic = system_of_equations_parser(equations_str, is_q)
    return {'sol': system_of_equations_solver(dic['matrix'], mod), 'vars': dic['vars']}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_determinant_result(mat_str, mod):
    is_q = False if mod != 0 else True
    mat = matrix_parser(mat_str, is_q)
    return determinant_solver(mat, mod)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_inverse_result(mat_str, mod):
    is_q = False if mod != 0 else True
    mat = matrix_parser(mat_str, is_q)
    return inverse_solver(mat, mod)

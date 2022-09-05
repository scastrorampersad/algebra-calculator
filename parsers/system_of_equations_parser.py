from fractions import Fraction as Frac
import numpy as np
import re

def generate_matrix(equation_list, is_q):
    vars = []

    for e in equation_list:
        vars += list(e.keys())

    vars_sorted = list(set(vars))
    vars_sorted.sort()

    matrix = np.zeros((len(equation_list), len(vars_sorted)), int)
    if is_q: matrix = matrix + Frac()

    for (row, equ) in zip(range(len(matrix)), equation_list):
        for col in range(len(vars_sorted)):
            if (e := equ.get(vars_sorted[col])) != None:
                matrix[row][col] = e

    return {'matrix': matrix, 'vars': vars_sorted}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def group_terms(left_side, right_side):
    dic = {}
    vars = set(list(left_side.keys()) + list(right_side.keys()))

    for v in vars:
        l = left_side.get(v)
        r = right_side.get(v)

        if l != None and r != None:
            dic[v] = l - r
        elif r != None:
            dic[v] = r * -1
        else:
            dic[v] = l

    if dic.get('~') != None:
        dic['~'] = dic['~'] * -1
    else:
        dic['~'] = 0

    return dic

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def to_term_dic(term_list, is_q):
    dic = {}

    for e in term_list:
        if e[-1].isalpha():
            if not e[-2].isnumeric():
                e = e[0] + '1' + e[1]
            if is_q:
                dic[e[-1]] = Frac(e[:-1])
            else:
                dic[e[-1]] = int(e[:-1])
        else:
            if is_q:
                dic['~'] = Frac(e)
            else:
                dic['~'] = int(e)

    return dic

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def split_terms(expression):
    terms = re.split('\-|\+', expression)
    signs = re.findall('[\-,\+]', expression)
    final_list = []

    if terms[0] == '':
        terms.remove('')
    else:
        signs.insert(0, '+')

    for (sign, term) in zip(signs, terms):
        final_list.append(f'{sign}{term}')

    return final_list

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def split_eqaution(equation, is_q):
    pattern_q = ('(-?([1-9](\d{1,3})?\/[1-9](\d{1,3})?|[1-9](\d{1,3})?)[a-z]'
    +'|-?([1-9](\d{1,3})?\/[1-9](\d{1,3})?|\d{1,4})|-?[a-z])([\-,\+]([1-9](\d{'
    +'1,3})?\/[1-9](\d{1,3})?|[1-9](\d{1,3})?)[a-z]|[\-,\+]([1-9](\d{1,3})?\/['
    +'1-9](\d{1,3})?|\d{1,4})|[\-,\+][a-z])*')
    pattern_z = ('(-?[1-9](\d{1,3})?[a-z]|-?\d{1,4}|-?[a-z])([\-,\+][1-9](\d{1'
    +',3})?[a-z]|[\-,\+]\d{1,4}|[\-,\+][a-z])*')
    pattern_list = [f'{pattern_q}={pattern_q}', f'{pattern_z}={pattern_z}']

    idx = 0 if is_q else 1
    equ_aux = equation.strip()

    if (re.match(pattern_list[idx], equ_aux) and re.match('\d{1,4}=\d{1,4}', equ_aux) == None
    and re.match('\d{1,4}\/\d{1,4}=\d{1,4}\/\d{1,4}', equ_aux) == None):
        return equ_aux.split('=')

    else:
        raise ValueError('Invalid_input')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def system_of_equations_parser(equs, is_q):
    equations_list_input = equs.split('\n')
    temp_result = []

    for e in equations_list_input:
        two_sides = split_eqaution(e, is_q)
        grouped_form = group_terms(to_term_dic(split_terms(two_sides[0]), is_q),
        to_term_dic(split_terms(two_sides[1]), is_q))
        temp_result.append(grouped_form)

    return generate_matrix(temp_result, is_q)

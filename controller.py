import sys
sys.path.append("diophantine")
sys.path.append("congruence")
sys.path.append("system_of_equations")
sys.path.append("determinant")
sys.path.append("inverse")

from launcher_view import LauncherView
from diophantine_view import DiophantineView
from congruence_view import CongruenceView
from system_of_equations_view import SystemOfEquationsView
from determinant_view import DeterminantView
from inverse_view import InverseView
from general_solver import *

class Controller():
    def __init__(self, launcher_view):
        self.launcher_view = launcher_view
        self.launcher_view.register_controller(self)
        self.diophantine_view = None
        self.congruence_view = None
        self.system_view = None
        self.determinant_view = None
        self.inverse_view = None
        self.mods = {'ℚ': 0, 'ℤ₂': 2, 'ℤ₃': 3, 'ℤ₅': 5,
        'ℤ₇': 7, 'ℤ₁₁': 11, 'ℤ₁₃': 13, 'ℤ₁₇': 17}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_sensitive_button_launcher(self, button_name, state):
        self.launcher_view.set_sensitive_button(button_name, state)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_determinant_button_clicked(self, widget):
        self.determinant_view = DeterminantView()
        self.launcher_view.set_sensitive_button('determinant', False)
        self.determinant_view.register_controller(self)
        self.determinant_view.start()

    def on_resolve_determinant_button_clicked(self, widget):
        mat_str = self.determinant_view.get_input_matrix()
        mod_str = self.determinant_view.get_input_mod()

        try:
            result = get_determinant_result(mat_str, self.mods[mod_str])
            self.determinant_view.set_result(result)
        except ValueError:
            self.determinant_view.generate_error_dialog('Invalid Input')
        except KeyError:
            self.determinant_view.generate_error_dialog('Field not selected')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_inverse_button_clicked(self, widget):
        self.inverse_view = InverseView()
        self.launcher_view.set_sensitive_button('inverse', False)
        self.inverse_view.register_controller(self)
        self.inverse_view.start()

    def on_resolve_inverse_button_clicked(self, widget):
        mat_str = self.inverse_view.get_input_matrix()
        mod_str = self.inverse_view.get_input_mod()

        try:
            result_mat = get_inverse_result(mat_str, self.mods[mod_str])
            result_str = ''

            if not result_mat['exist']:
                result_str = 'The matrix A does not have an inverse'
            else:
                for line in result_mat['inverse']:
                    line_str = list(map(str, line))
                    result_str += '   '.join(line_str) + '\n\n'

            self.inverse_view.set_result(result_str)
        except ValueError:
            self.inverse_view.generate_error_dialog('Invalid Input')
        except KeyError:
            self.inverse_view.generate_error_dialog('Field not selected')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_system_button_clicked(self, widget):
        self.system_view = SystemOfEquationsView()
        self.launcher_view.set_sensitive_button('system', False)
        self.system_view.register_controller(self)
        self.system_view.start()

    def on_resolve_system_button_clicked(self, widget):
        mod_str = self.system_view.get_input_mod()
        equations_str = self.system_view.get_input_equations()

        try:
            result = get_system_result(equations_str, self.mods[mod_str])

            vars = result['vars']
            sys_type = result['sol']['type']
            result['sol'].pop('type')

            result_str = 'System type: ' + sys_type + '\n\n'
            solutions = list(result['sol'].values())

            if sys_type == 'Consistent independent':
                for (var, sol) in zip(vars, solutions):
                    result_str += var + ' = ' + str(sol) + '\n\n'
            elif sys_type == 'Consistent dependent':
                for (var, generic_var) in zip(vars, list(result['sol'].keys())):
                    for i in range(len(solutions)):
                        solutions[i] = solutions[i].replace(generic_var, var)
                for (var, sol) in zip(vars, solutions):
                    if sol == '':
                        result_str += '∀ ' + var + ' ∈ ' + mod_str + '\n\n'
                    else:
                        result_str += var + ' = ' + sol.strip('+') + '\n\n'

            self.system_view.set_result(result_str)
        except ValueError:
            self.system_view.generate_error_dialog('Invalid Input')
        except KeyError:
            self.system_view.generate_error_dialog('Field not selected')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_diophantine_button_clicked(self, widget):
        self.diophantine_view = DiophantineView()
        self.launcher_view.set_sensitive_button('diophantine', False)
        self.diophantine_view.register_controller(self)
        self.diophantine_view.start()

    def on_resolve_diophantine_button_clicked(self, widget):
        equation_str = self.diophantine_view.get_input()

        try:
            result = get_diophantine_result(equation_str)

            if result != {}:
                str_result = 'x = ' + str(result['x'][0])
                if result['x'][1] >= 0:
                    str_result += '+'
                str_result += str(result['x'][1]) + 't'

                str_result += ' ' * 3 + 'y = ' + str(result['y'][0])
                if result['y'][1] >= 0:
                    str_result += '+'
                str_result += str(result['y'][1]) + 't'
            else:
                str_result = 'There is no solution'

            self.diophantine_view.set_result(str_result)

        except ValueError:
            self.diophantine_view.generate_error_dialog()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def on_congruence_button_clicked(self, widget):
        self.congruence_view = CongruenceView()
        self.launcher_view.set_sensitive_button('congruence', False)
        self.congruence_view.register_controller(self)
        self.congruence_view.start()

    def on_resolve_congruence_button_clicked(self, widget):
        equ_parms_str = self.congruence_view.get_input()

        try:
            result = get_congruence_result(equ_parms_str)
            str_result = ''
            line_size = 0

            if result == []:
                str_result = 'There is no solution'
            else:
                for x in result:
                    s = str(x)
                    line_size += len(s) + 1
                    if line_size > 41:
                        str_result += s + '\n'
                        line_size = 0
                    else:
                        str_result += s + ', '
                str_result = str_result.removesuffix(', ')

            self.congruence_view.set_result(str_result)

        except ValueError:
            self.congruence_view.generate_error_dialog()

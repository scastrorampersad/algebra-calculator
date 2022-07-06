# Copyright (c) 2022
# Sebastian Alfredo Castro Rampersad
# Santiago Alfredo Castro Rampersad
# All rights reserved

from launcher_v import launcher_view

class launcher_controller():
    def __init__(self, view):
        self.view = view
        self.view.register_controller(self)

    def on_determinant_button_clicked(self, widget):
        print("1")

    def on_inverse_button_clicked(self, widget):
        print("2")

    def on_system_button_clicked(self, widget):
        print("3")

    def on_diophantine_button_clicked(self, widget):
        print("4")

    def on_congruence_button_clicked(self, widget):
        print("5")

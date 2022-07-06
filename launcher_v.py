# Copyright (c) 2022
# Sebastian Alfredo Castro Rampersad
# Santiago Alfredo Castro Rampersad
# All rights reserved

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf, GLib

class launcher_view():
    def __init__(self):
        self.win = Gtk.Window(title = "Algebra Calculator")
        self.win.set_default_size(width = 300, height = 480)
        self.win.set_resizable(False)

        self.button_1 = Gtk.Button(label = "  Determinant of a matrix  ")
        self.button_2 = Gtk.Button(label = "       Inverse of a matrix       ")
        self.button_3 = Gtk.Button(label = "       System of equations       ")
        self.button_4 = Gtk.Button(label = "  Diophantine equation  ")
        self.button_5 = Gtk.Button(label = " Congruence enquations ")

        self.grid = Gtk.Grid()

        self.grid.set_margin_start(44)
        self.grid.set_margin_top(30)
        self.grid.set_row_spacing(30)

        self.grid.attach(self.button_1, left = 0, top = 0, width = 1, height = 3)
        self.grid.attach_next_to(self.button_2, self.button_1, Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.button_3, self.button_2, Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.button_4, self.button_3, Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.button_5, self.button_4, Gtk.PositionType.BOTTOM, 1, 3)

        self.win.add(self.grid)

    def start(self):
        self.win.connect("destroy", Gtk.main_quit)
        self.win.show_all()
        Gtk.main()

    def register_controller(self, controller):
        self.button_1.connect("clicked", controller.on_determinant_button_clicked)
        self.button_2.connect("clicked", controller.on_inverse_button_clicked)
        self.button_3.connect("clicked", controller.on_system_button_clicked)
        self.button_4.connect("clicked", controller.on_diophantine_button_clicked)
        self.button_5.connect("clicked", controller.on_congruence_button_clicked)

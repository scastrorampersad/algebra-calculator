import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf, GLib

class LauncherView():
    def __init__(self):
        self.win = Gtk.Window(title = "Algebra Calculator")
        self.win.set_default_size(width = 300, height = 480)
        self.win.set_resizable(False)

        self.buttons_map = {}

        self.buttons_map['determinant'] = Gtk.Button(label = "  Determinant of a matrix  ")
        self.buttons_map['inverse'] = Gtk.Button(label = "       Inverse of a matrix       ")
        self.buttons_map['system'] = Gtk.Button(label = "       System of equations       ")
        self.buttons_map['diophantine'] = Gtk.Button(label = "  Diophantine equation  ")
        self.buttons_map['congruence'] = Gtk.Button(label = " Congruence enquation ")

        self.grid = Gtk.Grid()

        self.grid.set_margin_start(44)
        self.grid.set_margin_top(30)
        self.grid.set_row_spacing(30)

        self.grid.attach(self.buttons_map['determinant'], left = 0, top = 0, width = 1, height = 3)
        self.grid.attach_next_to(self.buttons_map['inverse'], self.buttons_map['determinant'], Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.buttons_map['system'], self.buttons_map['inverse'], Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.buttons_map['diophantine'], self.buttons_map['system'], Gtk.PositionType.BOTTOM, 1, 3)
        self.grid.attach_next_to(self.buttons_map['congruence'], self.buttons_map['diophantine'], Gtk.PositionType.BOTTOM, 1, 3)

        self.win.add(self.grid)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def register_controller(self, controller):
        self.buttons_map['determinant'].connect("clicked", controller.on_determinant_button_clicked)
        self.buttons_map['inverse'].connect("clicked", controller.on_inverse_button_clicked)
        self.buttons_map['system'].connect("clicked", controller.on_system_button_clicked)
        self.buttons_map['diophantine'].connect("clicked", controller.on_diophantine_button_clicked)
        self.buttons_map['congruence'].connect("clicked", controller.on_congruence_button_clicked)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_sensitive_button(self, button_name, state):
        self.buttons_map[button_name].set_sensitive(state);

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def start(self):
        self.win.connect("destroy", Gtk.main_quit)
        self.win.show_all()
        Gtk.main()

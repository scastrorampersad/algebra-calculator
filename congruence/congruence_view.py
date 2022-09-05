import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf, GLib

class CongruenceView():
    def __init__(self):
        self.win = Gtk.Window(title = "Congruence equation")
        self.win.set_default_size(width = 400, height = 250)
        self.win.set_resizable(False)

        self.controller = None

        self.error_dialog = Gtk.MessageDialog(
            transient_for = self.win,
            flags = 0,
            message_type = Gtk.MessageType.ERROR,
            buttons = Gtk.ButtonsType.OK,
        )

        self.main_grid = Gtk.Grid()

        self.grid = Gtk.Grid()
        self.grid.set_margin_start(75)
        self.grid.set_margin_top(40)
        self.grid.set_row_spacing(10)

        self.box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0, halign = Gtk.Align.CENTER)
        self.box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5, halign = Gtk.Align.START)
        self.main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, halign = Gtk.Align.START)

        self.x_equi_label = Gtk.Label(label = 'x      ≡')
        self.mod_label = Gtk.Label(label = 'mod: ')
        self.result_label = Gtk.Label(label = "       Results:", halign = Gtk.Align.START)

        self.resolve_button = Gtk.Button(label = "Resolve")

        self.text_entry_a = Gtk.Entry()
        self.text_entry_mod = Gtk.Entry()
        self.text_entry_b = Gtk.Entry()

        self.scrolled_window = Gtk.ScrolledWindow(hexpand = True, vexpand = True)
        self.results_view = Gtk.TextView()
        self.results_view.set_editable(False)
        self.results_view.set_cursor_visible(False)

        self.scrolled_window.add(self.results_view)
        self.scrolled_window.set_margin_start(20)
        self.scrolled_window.set_margin_end(20)
        self.scrolled_window.set_margin_bottom(20)

        self.text_entry_a.set_width_chars(3)
        self.text_entry_a.set_alignment(1)
        self.text_entry_mod.set_width_chars(3)
        self.text_entry_b.set_width_chars(3)

        self.box_1.pack_start(self.text_entry_a, expand = False, fill = False, padding = 0)
        self.box_1.pack_start(self.x_equi_label, expand = False, fill = False, padding = 10)
        self.box_1.pack_start(self.text_entry_b, expand = False, fill = False, padding = 10)
        self.box_1.pack_start(self.resolve_button, expand = False, fill = False, padding = 0)
        self.grid.attach(self.box_1, left = 0, top = 0, width = 1, height = 1)

        self.box_2.pack_start(self.mod_label, expand = False, fill = False, padding = 0)
        self.box_2.pack_start(self.text_entry_mod, expand = False, fill = False, padding = 0)
        self.box_2.set_margin_start(20)
        self.grid.attach_next_to(self.box_2, self.box_1, Gtk.PositionType.BOTTOM, 1, 1)

        self.main_box.pack_start(self.grid, expand = False, fill = False, padding = 0)
        self.main_box.pack_start(self.result_label, expand = False, fill = False, padding = 10)
        self.main_grid.attach(self.main_box, left = 0, top = 0, width = 1, height = 1)

        self.main_grid.attach_next_to(self.scrolled_window, self.main_box, Gtk.PositionType.BOTTOM, 1, 1)

        self.win.add(self.main_grid)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_input(self):
        return {'a': self.text_entry_a.get_text(),
        'b': self.text_entry_b.get_text(), 'mod': self.text_entry_mod.get_text()}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_result(self, result):
        text_buffer = self.results_view.get_buffer()
        text_buffer.set_text(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def generate_error_dialog(self):
        self.error_dialog.set_markup('<b>Error</b>')
        self.error_dialog.format_secondary_text('Invalid Input')
        self.error_dialog.run()
        self.error_dialog.hide()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def register_controller(self, controller):
        self.controller = controller
        self.resolve_button.connect("clicked", controller.on_resolve_congruence_button_clicked)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def start(self):
        self.win.connect("destroy", self.close)
        self.win.show_all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def close(self, arg1 = None):
        self.controller.set_sensitive_button_launcher('congruence', True)
        self.win.destroy()

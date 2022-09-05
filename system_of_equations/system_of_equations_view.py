import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf, GLib

class SystemOfEquationsView():
    def __init__(self):
        self.win = Gtk.Window(title = "System of equations")
        self.win.set_default_size(width = 400, height = 400)
        self.win.set_resizable(False)

        self.controller = None

        self.error_dialog = Gtk.MessageDialog(
            transient_for = self.win,
            flags = 0,
            message_type = Gtk.MessageType.ERROR,
            buttons = Gtk.ButtonsType.OK,
        )

        self.main_grid = Gtk.Grid()

        self.label_equ = Gtk.Label(label = 'Equations:', halign = Gtk.Align.START)
        self.label_equ.set_margin_top(10)
        self.label_equ.set_margin_bottom(10)
        self.label_equ.set_margin_start(20)

        self.scrolled_window_equ = Gtk.ScrolledWindow(hexpand = True, vexpand = True)
        self.text_view_equ = Gtk.TextView()
        self.scrolled_window_equ.add(self.text_view_equ)

        self.scrolled_window_equ.set_margin_start(20)
        self.scrolled_window_equ.set_margin_end(20)
        self.scrolled_window_equ.set_margin_bottom(20)

        self.mod_combo_box = Gtk.ComboBoxText()
        self.mod_combo_box.append_text('ℚ')
        self.mod_combo_box.append_text('ℤ₂')
        self.mod_combo_box.append_text('ℤ₃')
        self.mod_combo_box.append_text('ℤ₅')
        self.mod_combo_box.append_text('ℤ₇')
        self.mod_combo_box.append_text('ℤ₁₁')
        self.mod_combo_box.append_text('ℤ₁₃')
        self.mod_combo_box.append_text('ℤ₁₇')

        self.label_mod = Gtk.Label(label = 'Field:')
        self.resolve_button = Gtk.Button(label = "Resolve")

        self.label_res = Gtk.Label(label = 'Results:', halign = Gtk.Align.START)
        self.label_res.set_margin_top(10)
        self.label_res.set_margin_bottom(10)
        self.label_res.set_margin_start(20)

        self.scrolled_window_res = Gtk.ScrolledWindow(hexpand = True, vexpand = True)
        self.text_view_res = Gtk.TextView()
        self.text_view_res.set_editable(False)
        self.text_view_res.set_cursor_visible(False)
        self.scrolled_window_res.add(self.text_view_res)

        self.scrolled_window_res.set_margin_start(20)
        self.scrolled_window_res.set_margin_end(20)
        self.scrolled_window_res.set_margin_bottom(20)

        self.box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0, halign = Gtk.Align.CENTER)
        self.box.set_margin_start(33)
        self.box.pack_start(self.label_mod, expand = False, fill = False, padding = 5)
        self.box.pack_start(self.mod_combo_box, expand = False, fill = False, padding = 0)
        self.box.pack_start(self.resolve_button, expand = False, fill = False, padding = 20)
        self.box.set_margin_end(17)

        self.main_grid.attach(self.label_equ, left = 0, top = 0, width = 1, height = 1)
        self.main_grid.attach_next_to(self.scrolled_window_equ, self.label_equ, Gtk.PositionType.BOTTOM, 1, 1)
        self.main_grid.attach_next_to(self.box, self.scrolled_window_equ, Gtk.PositionType.BOTTOM, 1, 1)
        self.main_grid.attach_next_to(self.label_res, self.box, Gtk.PositionType.BOTTOM, 1, 1)
        self.main_grid.attach_next_to(self.scrolled_window_res, self.label_res, Gtk.PositionType.BOTTOM, 1, 1)

        self.win.add(self.main_grid)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_input_equations(self):
        text_buffer = self.text_view_equ.get_buffer()
        s_iter = text_buffer.get_start_iter()
        e_iter = text_buffer.get_end_iter()
        return text_buffer.get_text(s_iter, e_iter, True)

    def get_input_mod(self):
        return self.mod_combo_box.get_active_text()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_result(self, result):
        text_buffer = self.text_view_res.get_buffer()
        text_buffer.set_text(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def generate_error_dialog(self, message):
        self.error_dialog.set_markup('<b>Error</b>')
        self.error_dialog.format_secondary_text(message)
        self.error_dialog.run()
        self.error_dialog.hide()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def register_controller(self, controller):
        self.controller = controller
        self.resolve_button.connect("clicked", controller.on_resolve_system_button_clicked)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def start(self):
        self.win.connect("destroy", self.close)
        self.win.show_all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def close(self, arg1 = None):
        self.controller.set_sensitive_button_launcher('system', True)
        self.win.destroy()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf, GLib

class DiophantineView():
    def __init__(self):
        self.win = Gtk.Window(title = "Diophantine equation")
        self.win.set_default_size(width = 400, height = 200)
        self.win.set_resizable(False)

        self.controller = None

        self.error_dialog = Gtk.MessageDialog(
            transient_for = self.win,
            flags = 0,
            message_type = Gtk.MessageType.ERROR,
            buttons = Gtk.ButtonsType.OK,
        )

        self.text_entry = Gtk.Entry()
        self.resolve_button = Gtk.Button(label = "Resolve")
        self.label_result = Gtk.Label(label = 'x =' + ' ' * 12 + 'y =' + ' ' * 6)

        self.grid = Gtk.Grid()
        self.grid.set_margin_start(58)
        self.grid.set_margin_top(40)
        self.grid.set_row_spacing(40)

        self.box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0, halign = Gtk.Align.CENTER)
        self.box.pack_start(self.text_entry, expand = False, fill = False, padding = 10)
        self.box.pack_start(self.resolve_button, expand = False, fill = False, padding = 0)

        self.grid.attach(self.box, left = 0, top = 0, width = 1, height = 1)
        self.grid.attach_next_to(self.label_result, self.box, Gtk.PositionType.BOTTOM, 1, 1)

        self.win.add(self.grid)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_input(self):
        return self.text_entry.get_text()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def set_result(self, result):
        self.label_result.set_text(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def generate_error_dialog(self):
        self.error_dialog.set_markup('<b>Error</b>')
        self.error_dialog.format_secondary_text('Invalid Input')
        self.error_dialog.run()
        self.error_dialog.hide()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def register_controller(self, controller):
        self.controller = controller
        self.resolve_button.connect("clicked", controller.on_resolve_diophantine_button_clicked)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def start(self):
        self.win.connect("destroy", self.close)
        self.win.show_all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def close(self, arg1 = None):
        self.controller.set_sensitive_button_launcher('diophantine', True)
        self.win.destroy()

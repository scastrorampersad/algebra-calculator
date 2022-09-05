#!/usr/bin/python3

from launcher_view import LauncherView
from controller import Controller

launcher_window = LauncherView()
Controller(launcher_window)
launcher_window.start()

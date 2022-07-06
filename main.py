#!/usr/bin/python3

# Copyright (c) 2022
# Sebastian Alfredo Castro Rampersad
# Santiago Alfredo Castro Rampersad
# All rights reserved

import sys
sys.path.append(".")

from launcher_v import launcher_view
from launcher_c import launcher_controller

launcher_window = launcher_view()
launcher_controller(launcher_window)
launcher_window.start()

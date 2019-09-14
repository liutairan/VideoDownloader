#!/usr/bin/env python

import sys
import os
import string
from random import *
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtGui import QIcon

from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Pics', 'icon.png')
    app.setWindowIcon(QIcon(path))
    mainWindow = MainWindow()
    sys.exit(app.exec_())

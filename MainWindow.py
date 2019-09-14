import sys
import os
import string
import math
from random import *
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton,
    QListWidget, QListWidgetItem, QAbstractItemView, QWidget, QAction,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout,
    QHeaderView, QLabel, QTreeWidget, QTreeWidgetItem, QToolBar, QLineEdit,
    QCompleter, QSizePolicy, QComboBox, QMessageBox, QDialog, QDialogButtonBox,
    QFileDialog, QStatusBar, QTabWidget, QFormLayout, QRadioButton)
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QStringListModel, QRect, QSize, Qt

from apscheduler.schedulers.background import BackgroundScheduler

from HeaderWidget import HeaderWidget
from DownloadWorker import DownloadWorker

class MainWindow(QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.connectionStatus = False
        self.initUI()

    def initUI(self):
        self.title = 'Video Downloader v0.0'
        self.left = 0
        self.top = 0
        self.width = 1080
        self.height = 720
        self.toolbarheight = 65
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.centerWindow()
        self.bundle_dir = os.path.dirname(os.path.abspath(__file__))
        self.initWidgets()
        self.setFocus()

    def centerWindow(self):
        frameGeo = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGeo.moveCenter(centerPoint)
        self.move(frameGeo.topLeft())

    def initWidgets(self):
        # HeaderBar
        self.headerWidget = HeaderWidget(self)
        self.headerWidget.setGeometry(0, 0, self.width, 100)
        self.headerWidget.show()
        # Show
        self.show()

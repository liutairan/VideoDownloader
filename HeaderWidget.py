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

from DownloadWorker import DownloadWorker

class HeaderWidget(QWidget):
    resized = pyqtSignal()
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.bundle_dir = os.path.dirname(os.path.abspath(__file__))
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Click the button to show data"))
        self.button = QPushButton("Extract Info",self)
        self.button.clicked.connect(self.processClick)
        self.layout.addWidget(self.button)
        self.initWidgets()
        self.setLayout(self.layout)

    def centerWindow(self):
        frameGeo = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGeo.moveCenter(centerPoint)
        self.move(frameGeo.topLeft())

    def initWidgets(self):
        pass

    def processClick(self):
        self.worker = DownloadWorker()
        link = "https://www.youtube.com/watch?v=NWaTWj7cLKc"
        self.worker.extractInfo([link])

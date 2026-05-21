import sys

from PySide6.QtCore import QRect
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("OmniOrganizer")
        screen: QScreen = QApplication.primaryScreen()
        screen_size: QRect = screen.availableGeometry()
        self.width = 800
        self.height = 600
        self.setGeometry((screen_size.width()-self.width)//2,
                         (screen_size.height()-self.height)//2,
                         self.width, self.height)
        self.label: QLabel = QLabel("Hello, PySide6!", self)
        self.label.setGeometry(100, 100, 400, 200)
        self.show()
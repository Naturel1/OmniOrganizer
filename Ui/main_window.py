from PySide6.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My First PySide6 App")
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel("Hello, PySide6!", self)
        self.label.setGeometry(100, 100, 400, 200)
        self.show()
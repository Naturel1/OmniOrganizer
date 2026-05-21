import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication

from Ui.main_window import MainWindow


@Slot()
def say_hello():
    print("Button hello Clicked !")

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()

if __name__ == "__main__":
    main()
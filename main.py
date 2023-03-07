import sys

from PySide6.QtWidgets import QApplication
from controller.main_controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show()
    app.exec()

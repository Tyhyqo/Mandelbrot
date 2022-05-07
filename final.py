import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Mand(QMainWindow):
    def __init__(self):
        super().__init__()
        # Параметры окна
        self.setFixedSize()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    mand = Mand()
    mand.show()
    sys.exit(app.exec())

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Mand(QWidget):
    def __init__(self):
        super().__init__()
        # initUI
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Серый Мандельброт')
        self.qp = QPainter()
        # Количество итераций
        self.max_iteration = 255
        # Создание палитры
        self.palette = [
            (
                int(255 * math.sin(i / 30.0 + 0.5) ** 2),
                int(255 * math.sin(i / 30.0 + 0.0) ** 2),
                int(255 * math.sin(i / 30.0 + 0.5) ** 2),
            ) for i in range(self.max_iteration - 1)
        ]
        self.palette.append((0, 0, 0))

    def paintEvent(self, event):
        self.qp.begin(self)
        self.mand_color()
        self.qp.end()

    def mand_color(self):
        # Комплексное поле и его размеры
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        # Размеры окна
        img_x, img_y = self.width(), self.height()
        # Рисование
        for y in range(img_y):
            # Найдём комплексную ординату точки
            zy = y * (yb - ya) / img_y + ya
            for x in range(img_x):
                # Найдём комплексную абсциссу точки
                zx = x * (xb - xa) / img_x + xa
                # Зададим начальные параметры последовательности
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                pen = QPen(QColor(*self.palette[cnt]), 1)
                self.qp.setPen(pen)
                self.qp.drawPoint(QPoint(x, y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mand = Mand()
    mand.show()
    sys.exit(app.exec())

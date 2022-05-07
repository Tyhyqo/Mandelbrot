import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Mand(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Чёрно-белый Мандельброт')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.mand_bw(qp)
        qp.end()

    def mand_bw(self, qp):
        # Комплексное поле и его размеры
        xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
        # Количество итераций
        max_iteration = 255
        # Размеры окна
        img_x, img_y = self.width(), self.height()
        # Параметры пера
        pen = QPen(Qt.black, 1)
        qp.setPen(pen)
        # Рисование
        for y in range(img_y):
            # Найдём комплексную ординату точки
            zy = y * (yb - ya) / img_y + ya
            for x in range(img_x):
                # Найдём комплексную абсциссу точки
                zx = x * (xb - xa) / img_x + xa
                # Зададим начальные параметры последовательности
                c, z = zx + zy * 1j, 0
                for cnt in range(max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                if cnt == max_iteration - 1:
                    qp.drawPoint(QPoint(x, y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mand = Mand()
    mand.show()
    sys.exit(app.exec())

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QColor, QPainter, QImage, QFont
from PyQt6 import QtCore
from PyQt6.QtWidgets import QFileDialog


def drawChessBoard(self, qp, n):
    """Отрисовка сетки и текста"""

    base_n = n
    n = n * 2
    even = (n % 2 == 0)

    w = self.width() / (n - 1)
    h = (self.height() - self.y_offset) / (n - 1)
    MENU_OFFSET = 20    # 20 пикселей по Y для корректной отрисовки меню

    self.spins = []
    self.ver = []
    self.hor = []

    _ignore = 0

    # выбор цветов

    if self.background_color == 0:
        color_spin = QColor(220, 220, 220)
        color_empty = QColor(255, 255, 255)
    elif self.background_color == 1:
        color_spin = QColor(255, 255, 255)
        color_empty = QColor(255, 255, 255)
    else:
        color_spin = QColor(220, 220, 220)
        color_empty = QColor(220, 220, 220)

    # размер шрифта
    font = QFont();
    font.setPixelSize(12);

    hi = 0; vi = 0
    x = 0; y = 0
    temp = 0
    for i in range(n - 1):
        for j in range(n):
            spin = False; verJ = False; horJ = False

            if temp == 0:
                if j % 2 == 0:
                    qp.setBrush(color_spin)
                    spin = True
                else:
                    qp.setBrush(color_empty)
                temp += 1
            else:
                if i % 2 != 0:
                    verJ = True
                    if self.verJ_val[vi] == 1:
                        qp.setBrush(QColor(255, 170, 170))
                    elif self.verJ_val[vi] == -1:
                        qp.setBrush(QColor(170, 170, 255))
                    else:
                        qp.setBrush(color_empty)
                    vi += 1
                    pass
                else:
                    horJ = True
                    _ignore += 1
                    if _ignore % base_n != 0:
                        if self.horJ_val[hi] == 1:
                            qp.setBrush(QColor(255, 170, 170))
                        elif self.horJ_val[hi] == -1:
                            qp.setBrush(QColor(170, 170, 255))
                        else:
                            qp.setBrush(color_empty)
                        hi += 1

                temp -= 1

            r = QRect(int(x), int(y + MENU_OFFSET), int(w), int(h))
            qp.drawRect(r)
            x += w

            if spin:
                self.spins.append(r)
            if verJ:
                self.ver.append(r)
            if horJ:
                if _ignore % base_n == 0:
                    _ignore = 0
                else:
                    self.hor.append(r)

        x = 0
        y += h
        if even:
            if temp == 0:
                temp = 1
            else:
                temp = 0

    self.ver = self.ver[:base_n * base_n - base_n]
    self.hor = self.hor[:base_n * base_n - base_n]

    if self.spins_drown:
        for i in range(len(self.spins)):
            if self.spins_val[i] == 0:
                qp.drawText(self.spins[i], QtCore.Qt.AlignmentFlag.AlignHCenter, '↓')
            elif self.spins_val[i] == 1:
                qp.drawText(self.spins[i], QtCore.Qt.AlignmentFlag.AlignHCenter, '↑')

    if self.numbers_drown:
        for i in range(len(self.ver)):
            qp.drawText(self.ver[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.verJ_val[i]))
        for i in range(len(self.hor)):
            qp.drawText(self.hor[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.horJ_val[i]))

    # print(self.spins_val)


def saveChessBoard(self, qp):
    fpath, _ = QFileDialog.getSaveFileName(None, 'Запись файла', '', 'png (*.png);;jpg (*.jpg);;bmp (*.bmp)')
    if fpath:
        image = QImage(self.size(), QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.transparent)

        painter = QPainter(image)
        self.render(painter)
        painter.end()

        rect_to_copy = QRect(0, 22, image.width(), image.height() - self.y_offset - 2)
        cropped_image = image.copy(rect_to_copy)

        cropped_image.save(fpath)
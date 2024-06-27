from PyQt6.QtCore import QRect
from PyQt6.QtGui import QColor
from PyQt6 import QtCore


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

    hi = 0; vi = 0
    x = 0; y = 0
    temp = 0
    for i in range(n - 1):
        for j in range(n):
            spin = False; verJ = False; horJ = False

            if temp == 0:
                if j % 2 == 0:
                    qp.setBrush(QColor(220, 220, 220))
                    spin = True
                else:
                    qp.setBrush(QColor(255, 255, 255))
                temp += 1
            else:
                if i % 2 != 0:
                    verJ = True
                    if self.verJ_val[vi] == 1:
                        qp.setBrush(QColor(255, 170, 170))
                    else:
                        qp.setBrush(QColor(170, 170, 255))
                    vi += 1
                    pass
                else:
                    horJ = True
                    _ignore += 1
                    if _ignore % base_n != 0:
                        if self.horJ_val[hi] == 1:
                            qp.setBrush(QColor(255, 170, 170))
                        else:
                            qp.setBrush(QColor(170, 170, 255))
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

    if self.numbers_drown:

        for i in range(len(self.spins)):
            if self.spins_val[i] == 0:
                qp.drawText(self.spins[i], QtCore.Qt.AlignmentFlag.AlignHCenter, '↓')
            elif self.spins_val[i] == 1:
                qp.drawText(self.spins[i], QtCore.Qt.AlignmentFlag.AlignHCenter, '↑')
        for i in range(len(self.ver)):
            qp.drawText(self.ver[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.verJ_val[i]))
        for i in range(len(self.hor)):
            qp.drawText(self.hor[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.horJ_val[i]))
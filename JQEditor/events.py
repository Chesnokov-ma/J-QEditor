from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtCore import Qt


def paintEvent(self, event):
    """Отрисовка графики с помощью QPainter"""
    if self.is_downloaded:
        qp = QPainter()
        qp.begin(self)
        qp.setFont(QFont('Decorative', 20))
        self.drawChessBoard(qp, self.n)
        qp.end()


def mousePressEvent(self, event):
    """Обработка нажатий мыши"""

    # если экран пустой
    # открыть окно выбора файла при нажатии
    if event.button() == Qt.MouseButton.LeftButton:
        if not self.is_downloaded:
            self.read_button_clicked()

    # координаты нажатия мышки
    if event.button() == Qt.MouseButton.LeftButton:
        click_pos = event.pos()
    else:
        click_pos = None

    if click_pos:
        # если нажатие в пределах координат прямоугольников, то инвертируем значение и перерисовываем
        vi = 0
        for rect in self.ver:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                # print(vi)
                self.verJ_val[vi] *= -1
            vi += 1

        hi = 0
        for rect in self.hor:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                # print(hi)
                self.horJ_val[hi] *= -1
            hi += 1

        if self.is_downloaded:
            self.update()


# def keyPressEvent(self, event):
#     """Обработка нажатия клавиш клавиатуры"""
#
#     # Инвертировать (Ctrl + I)
#     if event.modifiers() & Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_I:
#         if self.is_downloaded:
#             for i in range(len(self.verJ_val)):
#                 self.verJ_val[i] *= -1
#                 self.horJ_val[i] *= -1
#             self.update()


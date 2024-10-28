from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtCore import Qt


def paintEvent(self, event):
    """Отрисовка графики с помощью QPainter"""
    if self.is_downloaded:
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.setFont(QFont('Decorative', 20))
        self.drawChessBoard(self.qp, self.n)
        self.qp.end()


def mousePressEvent(self, event):
    """Обработка нажатий мыши"""

    left_mouse_btn_pressed = False
    middle_mouse_btn_pressed = False

    # если экран пустой
    # открыть окно выбора файла при нажатии
    if event.button() == Qt.MouseButton.LeftButton:
        if not self.is_downloaded:
            self.read_button_clicked()

    # координаты нажатия мышки
    if event.button() == Qt.MouseButton.LeftButton:
        left_mouse_btn_pressed = True
        click_pos = event.pos()
    elif event.button() == Qt.MouseButton.MiddleButton:
        middle_mouse_btn_pressed = True
        click_pos = event.pos()
    else:
        click_pos = None

    if click_pos and self.is_downloaded:
        # если нажатие в пределах координат прямоугольников, то инвертируем значение и перерисовываем
        vi = 0
        for rect in self.ver:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                if left_mouse_btn_pressed:
                    if self.verJ_val[vi] == 1 or self.verJ_val[vi] == -1:
                        self.verJ_val[vi] *= -1
                    else:
                        self.verJ_val[vi] = 1
                elif middle_mouse_btn_pressed:
                    if self.verJ_val[vi] == 0:
                        self.verJ_val[vi] = 1
                    else:
                        self.verJ_val[vi] = 0

            vi += 1

        hi = 0
        for rect in self.hor:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                if left_mouse_btn_pressed:
                    if self.horJ_val[hi] == -1 or self.horJ_val[hi] == 1:
                        self.horJ_val[hi] *= -1
                    else:
                        self.horJ_val[hi] = 1
                elif middle_mouse_btn_pressed:
                    if self.horJ_val[hi] == 0:
                        self.horJ_val[hi] = 1
                    else:
                        self.horJ_val[hi] = 0

            hi += 1

        # переворот спинов
        si = 0
        for rect in self.spins:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                if self.spins_val[si] == 1:
                    self.spins_val[si] = 0
                elif self.spins_val[si] == 0:
                    self.spins_val[si] = 1
            si += 1

        if self.is_downloaded:
            self.calc.update_info(self.calc_shown)
            self._update_app()


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


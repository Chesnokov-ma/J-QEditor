from PyQt6.QtGui import QPainter, QFont


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
    if not self.is_downloaded:
        self.read_button_clicked()

    # координаты нажатия мышки
    click_pos = event.pos()

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

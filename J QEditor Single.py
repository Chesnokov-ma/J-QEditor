from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtWidgets import QPushButton, QMessageBox
from PyQt6.QtCore import QRect, pyqtSlot
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6 import QtCore
from math import sqrt
import sys


"""J QEditor Single"""
class MainWindow(QMainWindow):
    n = None
    is_downloaded = False
    all_down = False
    J_full = []
    verJ_val = []; horJ_val = []
    spins = []; ver = []; hor = []
    y_offset = 100

    def __init__(self):
        # добавить виджеты
        super().__init__()
        self.setWindowTitle('J QEditor')
        self.resize(600, 600 + self.y_offset)
        self.main_widget = QWidget()
        paint_widget = QWidget()
        paint_widget.resize(600, 600)
        main_layout = QVBoxLayout()
        main_layout.addWidget(paint_widget)
        read_button = QPushButton('Выбрать файл')
        write_button = QPushButton('Записать в файл')
        self.all_down_button = QPushButton('Все -1')

        # добавить кнопки
        main_layout.addWidget(read_button)
        main_layout.addWidget(self.all_down_button)
        main_layout.addWidget(write_button)

        # установить main_widget как центральный виджет
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)

        # slots (привязка обработки)
        read_button.clicked.connect(self.read_button_clicked)
        write_button.clicked.connect(self.write_button_clicked)
        self.all_down_button.clicked.connect(self.all_down_button_clicked)

    @pyqtSlot()
    def read_button_clicked(self):
        # Кнопка чтения файла
        fpath = QFileDialog.getOpenFileName(caption='Чтение файла', filter="Data (*.dat *.txt);;All files (*.*)")[0]
        if fpath:
            try:
                self.n = int(sqrt(int(fpath.split('_')[0].replace('cell', '').split('/')[-1])))
                self.read_data(fpath)
            except:
                QMessageBox.critical(self, 'Ошибка!', 'Неправильный формат файла!')

    @pyqtSlot()
    def write_button_clicked(self):
        # Кнопка записи файла
        if self.is_downloaded:
            try:
                fpath, _ = QFileDialog.getSaveFileName(None, 'Запись файла', '.',  'Dat (*.dat);;Text (*.txt)')
                self.write_data(fpath)
            except:
                pass

    @pyqtSlot()
    def all_down_button_clicked(self):
        # Кнопка все +=1
        if self.is_downloaded:
            val = None
            if self.all_down:
                val = 1
                self.all_down = False
                self.all_down_button.setText('Все -1')
            else:
                val = -1
                self.all_down = True
                self.all_down_button.setText('Все +1')

            self.verJ_val = [val for _ in range(self.n * self.n - self.n)]
            self.horJ_val = [val for _ in range(self.n * self.n - self.n)]
            self.update()

    def read_data(self, file_name='./example'):
        # Прочитать решетку из файла
        self.verJ_val = [0 for _ in range(self.n * self.n - self.n)]
        self.horJ_val = [0 for _ in range(self.n * self.n - self.n)]

        self.J_full = []

        with open(file_name, 'r') as f:
            for line in f:
                for elem in line.replace(' \n', '').split(' '):
                    self.J_full.append(int(elem))

        k = 1
        for i in range(self.n):
            for j in range(self.n - 1):
                self.horJ_val[i * (self.n - 1) + j] = self.J_full[k]
                k += self.n * self.n + 1
            k += self.n * self.n + 1

        k = self.n
        for i in range(self.n - 1):
            for j in range(self.n):
                self.verJ_val[i * self.n + j] = self.J_full[k]
                k += self.n * self.n + 1

        self.is_downloaded = True
        self.update()

    def write_data(self, file_name):
        # Запись в файл (то же что и read_data(), только наоборот)
        k = 1
        for i in range(self.n):
            for j in range(self.n - 1):
                self.J_full[k] = self.horJ_val[i * (self.n - 1) + j]
                k += self.n * self.n + 1
            k += self.n * self.n + 1

        k = self.n
        for i in range(self.n - 1):
            for j in range(self.n):
                self.J_full[k] = self.verJ_val[i * self.n + j]
                k += self.n * self.n + 1

        with open(file_name, 'w') as f:
            symbols = 0
            for j in self.J_full:
                f.write(f'{j} ')
                symbols += 1
                if symbols == self.n * self.n:
                    f.write('\n')
                    symbols = 0

    def paintEvent(self, event):
        # отрисовка графики с помощью QPainter
        if self.is_downloaded:
            qp = QPainter()
            qp.begin(self)
            qp.setFont(QFont('Decorative', 20))
            self.drawChessBoard(qp, self.n)
            qp.end()

    def drawChessBoard(self, qp, n):
        # Нарисовать сетку и текст
        base_n = n
        n = n * 2
        even = (n % 2 == 0)

        w = self.width() / (n - 1)
        h = (self.height() - self.y_offset) / (n - 1)

        self.spins = []
        self.ver = []
        self.hor = []

        _ignore = 0

        hi = 0; vi = 0
        x = 0; y = 0; temp = 0
        for i in range(n - 1):
            for j in range(n):
                spin = False; verJ = False; horJ = False

                if temp == 0:
                    if j % 2 == 0:
                        qp.setBrush(QColor(220,220,220))
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

                r = QRect(int(x), int(y), int(w), int(h))
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

        for rect in self.spins:
            qp.drawText(rect, QtCore.Qt.AlignmentFlag.AlignHCenter, '↑')
        for i in range(len(self.ver)):
            qp.drawText(self.ver[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.verJ_val[i]))
        for i in range(len(self.hor)):
            qp.drawText(self.hor[i], QtCore.Qt.AlignmentFlag.AlignHCenter, str(self.horJ_val[i]))

    def mousePressEvent(self, event):
        # Обработка нажатия мыши

        click_pos = event.pos()

        # если нажатие в пределах координат прямоугольников, то инвертируем значение и перерисовываем

        vi = 0
        for rect in self.ver:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                print(vi)
                self.verJ_val[vi] *= -1
            vi += 1

        hi = 0
        for rect in self.hor:
            if (rect.x() + rect.width()) > click_pos.x() > rect.x() and (rect.y() + rect.height()) > click_pos.y() > rect.y():
                print(hi)
                self.horJ_val[hi] *= -1
            hi += 1

        if self.is_downloaded:
            self.update()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()